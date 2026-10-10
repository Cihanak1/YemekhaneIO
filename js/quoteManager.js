/**
 * quoteManager.js — v2.0
 * ──────────────────────────────────────────────────────────────
 * Yemekhane Panosu — Günlük Notlar Yönetimi
 *
 * Özellikler:
 *   • Yapay zeka / varsayılan hazır sözler içermez; yalnızca gerçek ziyaretçi notlarını gösterir.
 *   • Bulut senkronizasyonu (ntfy.sh JSON + gerçek zamanlı SSE akışı) ile siteye giren herkes
 *     yazılan notları ve yapılan düzenlemeleri anında görür.
 *   • Kullanıcı kendi yazdığı notu dilediği zaman düzenleyebilir veya silebilir.
 *   • Notlar yalnızca o güne aittir; gün sonunda (00:00) pano otomatik olarak sıfırlanır.
 */

'use strict';

const QuoteManager = (() => {

  const STORAGE_KEY      = 'yemekhane_daily_notes_v2';
  const CLIENT_TOKEN_KEY = 'yemekhane_client_token_v2';
  const MY_NOTES_KEY     = 'yemekhane_my_notes_v2';
  const LIKES_KEY        = 'yemekhane_liked_notes_v2';
  const NAME_KEY         = 'yemekhane_user_author_name';

  // Eski sürümden kalan anahtarları temizle
  const LEGACY_KEYS = ['yemekhane_quotes_v1', 'yemekhane_quote_likes_v1'];

  const CLOUD_BASE_URL   = 'https://ntfy.sh';
  const TOPIC_PREFIX     = 'yemekhane_io_gunluk_not_v2_';
  const POLL_INTERVAL_MS = 20000;

  const dateFmt = new Intl.DateTimeFormat('en-GB', {
    timeZone: 'Europe/Istanbul',
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
  });

  /* ── DURUM ─────────────────────────────────────────────────── */
  let todayDateKey   = '';
  let notesList      = [];          // Bugünün aktif notları (yeni -> eski)
  let deletedIdsSet  = new Set();   // Bugün silinen notların ID'leri
  let editingNoteId  = null;        // Düzenleme modundaysa düzenlenen notun ID'si
  let isSyncing      = false;
  let initialLoaded  = false;
  let eventSource    = null;
  let pollTimer      = null;
  let broadcastChan  = null;

  /* ── TARİH & KİMLİK YARDIMCILARI ───────────────────────────── */
  function getTodayDateKey(now = new Date()) {
    const p = {};
    for (const { type, value } of dateFmt.formatToParts(now)) {
      p[type] = value;
    }
    return `${p.day}.${p.month}.${p.year}`;
  }

  function getTopicForDate(dateKey) {
    return `${TOPIC_PREFIX}${String(dateKey).replace(/[^0-9]/g, '_')}`;
  }

  function getClientToken() {
    try {
      let token = localStorage.getItem(CLIENT_TOKEN_KEY);
      if (!token || token.length < 12) {
        const rand = Math.random().toString(36).substring(2) + Math.random().toString(36).substring(2);
        token = `usr_${Date.now().toString(36)}_${rand}`;
        localStorage.setItem(CLIENT_TOKEN_KEY, token);
      }
      return token;
    } catch (_) {
      if (!window.__yemekhaneTempToken) {
        window.__yemekhaneTempToken = `tmp_${Date.now()}_${Math.random().toString(36).substring(2)}`;
      }
      return window.__yemekhaneTempToken;
    }
  }

  function hashString(input) {
    const str = String(input || '');
    let h1 = 0xdeadbeef ^ str.length;
    let h2 = 0x41c6ce57 ^ str.length;
    for (let i = 0; i < str.length; i++) {
      const ch = str.charCodeAt(i);
      h1 = Math.imul(h1 ^ ch, 2654435761);
      h2 = Math.imul(h2 ^ ch, 1597334677);
    }
    h1 = Math.imul(h1 ^ (h1 >>> 16), 2246822507) ^ Math.imul(h2 ^ (h2 >>> 13), 3266489909);
    h2 = Math.imul(h2 ^ (h2 >>> 16), 2246822507) ^ Math.imul(h1 ^ (h1 >>> 13), 3266489909);
    return (h2 >>> 0).toString(36) + (h1 >>> 0).toString(36);
  }

  function computeOwnerHash(noteId) {
    return hashString(`${getClientToken()}:owner:${noteId}`);
  }

  function computeVoterHash(noteId) {
    return hashString(`${getClientToken()}:like:${noteId}`);
  }

  function getMyNoteIds() {
    try {
      const raw = localStorage.getItem(MY_NOTES_KEY);
      const parsed = raw ? JSON.parse(raw) : null;
      if (parsed && parsed.dateKey === todayDateKey && Array.isArray(parsed.ids)) {
        return parsed.ids;
      }
    } catch (_) {}
    return [];
  }

  function addMyNoteId(noteId) {
    const ids = getMyNoteIds();
    if (!ids.includes(noteId)) {
      ids.push(noteId);
      try {
        localStorage.setItem(MY_NOTES_KEY, JSON.stringify({
          dateKey: todayDateKey,
          ids
        }));
      } catch (_) {}
    }
  }

  function isOwnNote(note) {
    if (!note || !note.id) return false;
    const myIds = getMyNoteIds();
    if (myIds.includes(note.id)) return true;
    if (note.ownerHash && note.ownerHash === computeOwnerHash(note.id)) return true;
    return false;
  }

  function getLikedNoteIds() {
    try {
      const raw = localStorage.getItem(LIKES_KEY);
      const parsed = raw ? JSON.parse(raw) : null;
      if (parsed && parsed.dateKey === todayDateKey && Array.isArray(parsed.ids)) {
        return parsed.ids;
      }
    } catch (_) {}
    return [];
  }

  function saveLikedNoteIds(ids) {
    try {
      localStorage.setItem(LIKES_KEY, JSON.stringify({
        dateKey: todayDateKey,
        ids
      }));
    } catch (_) {}
  }

  function getSavedAuthorName() {
    try {
      return localStorage.getItem(NAME_KEY) || '';
    } catch (_) {
      return '';
    }
  }

  function setSavedAuthorName(name) {
    try {
      localStorage.setItem(NAME_KEY, name);
    } catch (_) {}
  }

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  /* ── YEREL ÖNBELLEK & GÜN SONU SIFIRLAMA ───────────────────── */
  function cleanupLegacyAndExpiredStorage() {
    LEGACY_KEYS.forEach(k => {
      try { localStorage.removeItem(k); } catch (_) {}
    });

    const currentToday = getTodayDateKey();
    [STORAGE_KEY, MY_NOTES_KEY, LIKES_KEY].forEach(key => {
      try {
        const raw = localStorage.getItem(key);
        if (!raw) return;
        const parsed = JSON.parse(raw);
        if (!parsed || parsed.dateKey !== currentToday) {
          localStorage.removeItem(key);
        }
      } catch (_) {
        try { localStorage.removeItem(key); } catch (__ ) {}
      }
    });
  }

  function loadLocalState() {
    cleanupLegacyAndExpiredStorage();
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return;
      const parsed = JSON.parse(raw);
      if (parsed && parsed.dateKey === todayDateKey) {
        if (Array.isArray(parsed.deletedIds)) {
          deletedIdsSet = new Set(parsed.deletedIds);
        }
        if (Array.isArray(parsed.notes)) {
          notesList = parsed.notes.filter(n => n && n.id && !deletedIdsSet.has(n.id) && n.dateKey === todayDateKey);
        }
      }
    } catch (_) {
      notesList = [];
      deletedIdsSet = new Set();
    }
  }

  function saveLocalState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({
        dateKey: todayDateKey,
        notes: notesList,
        deletedIds: Array.from(deletedIdsSet).slice(-100)
      }));
    } catch (_) {}
  }

  function notifyOtherTabs() {
    if (broadcastChan) {
      try {
        broadcastChan.postMessage({
          type: 'notes_updated',
          dateKey: todayDateKey
        });
      } catch (_) {}
    }
  }

  /* ── BULUT SENKRONİZASYONU (ntfy.sh) ───────────────────────── */
  function buildCompactSnapshot() {
    const snap = [];
    let approxBytes = 0;
    for (const n of notesList) {
      if (!n || deletedIdsSet.has(n.id)) continue;
      const item = {
        id: n.id,
        dateKey: todayDateKey,
        author: String(n.author || '').slice(0, 30),
        text: String(n.text || '').slice(0, 220),
        time: n.time || '',
        createdAt: n.createdAt || Date.now(),
        updatedAt: n.updatedAt || Date.now(),
        edited: Boolean(n.edited),
        likes: Number(n.likes) || 0,
        ownerHash: n.ownerHash || ''
      };
      const itemBytes = JSON.stringify(item).length;
      if (approxBytes + itemBytes > 2600) break;
      snap.push(item);
      approxBytes += itemBytes;
    }
    return snap;
  }

  async function publishCloudEvent(eventObj) {
    const topic = getTopicForDate(todayDateKey);
    const fullPayload = {
      v: 2,
      dateKey: todayDateKey,
      ...eventObj,
      deletedIds: Array.from(deletedIdsSet).slice(-40),
      snapshot: buildCompactSnapshot()
    };

    const body = JSON.stringify({
      topic,
      message: JSON.stringify(fullPayload)
    });

    try {
      await fetch(CLOUD_BASE_URL, {
        method: 'POST',
        body
      });
    } catch (err) {
      console.warn('[QuoteManager] Bulut gönderimi başarısız:', err);
    }
  }

  function applySingleCloudPayload(payload, notesMap, likesByNote) {
    if (!payload || payload.v !== 2) return;
    if (payload.dateKey && payload.dateKey !== todayDateKey) return;

    if (Array.isArray(payload.deletedIds)) {
      for (const delId of payload.deletedIds) {
        if (delId) {
          deletedIdsSet.add(delId);
          notesMap.delete(delId);
        }
      }
    }

    if (payload.action === 'delete' && payload.noteId) {
      const existing = notesMap.get(payload.noteId);
      if (!existing || !existing.ownerHash || existing.ownerHash === payload.ownerHash) {
        deletedIdsSet.add(payload.noteId);
        notesMap.delete(payload.noteId);
      }
    }

    if (Array.isArray(payload.snapshot)) {
      for (const snapNote of payload.snapshot) {
        if (!snapNote || !snapNote.id || deletedIdsSet.has(snapNote.id)) continue;
        if (snapNote.dateKey && snapNote.dateKey !== todayDateKey) continue;
        const existing = notesMap.get(snapNote.id);
        if (!existing || (snapNote.updatedAt || 0) >= (existing.updatedAt || 0)) {
          notesMap.set(snapNote.id, {
            ...existing,
            ...snapNote,
            dateKey: todayDateKey
          });
        }
      }
    }

    if (payload.action === 'add' && payload.note && payload.note.id) {
      const n = payload.note;
      if (!deletedIdsSet.has(n.id)) {
        const existing = notesMap.get(n.id);
        if (!existing || (n.updatedAt || 0) >= (existing.updatedAt || 0)) {
          notesMap.set(n.id, {
            ...existing,
            ...n,
            dateKey: todayDateKey
          });
        }
      }
    }

    if (payload.action === 'edit' && payload.noteId) {
      if (!deletedIdsSet.has(payload.noteId)) {
        const existing = notesMap.get(payload.noteId);
        if (existing && (!existing.ownerHash || existing.ownerHash === payload.ownerHash)) {
          if ((payload.updatedAt || 0) >= (existing.updatedAt || 0)) {
            existing.author = String(payload.author || existing.author || 'Anonim').slice(0, 30);
            existing.text = String(payload.text || existing.text || '').slice(0, 220);
            existing.edited = true;
            existing.updatedAt = payload.updatedAt || Date.now();
          }
        }
      }
    }

    if (payload.action === 'like' && payload.noteId && payload.voterHash) {
      if (!likesByNote.has(payload.noteId)) {
        likesByNote.set(payload.noteId, new Set());
      }
      const set = likesByNote.get(payload.noteId);
      if (payload.liked === false) {
        set.delete(payload.voterHash);
      } else {
        set.add(payload.voterHash);
      }
    }
  }

  function mergeAndCommitNotes(notesMap, likesByNote = new Map()) {
    for (const [noteId, voters] of likesByNote.entries()) {
      const note = notesMap.get(noteId);
      if (note) {
        note.likes = Math.max(Number(note.likes) || 0, voters.size);
      }
    }

    const merged = Array.from(notesMap.values())
      .filter(n => n && n.id && !deletedIdsSet.has(n.id) && n.text)
      .sort((a, b) => (b.createdAt || 0) - (a.createdAt || 0));

    notesList = merged;
    saveLocalState();
  }

  async function syncFromCloud() {
    checkDayRollover();
    if (isSyncing) return;
    isSyncing = true;

    const syncDateKey = todayDateKey;
    const topic = getTopicForDate(syncDateKey);
    const url = `${CLOUD_BASE_URL}/${encodeURIComponent(topic)}/json?poll=1&since=all&_t=${Date.now()}`;

    try {
      const res = await fetch(url, { cache: 'no-store' });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const text = await res.text();

      if (syncDateKey !== todayDateKey) return;

      const notesMap = new Map();
      const likesByNote = new Map();

      // Mevcut yerel notları başlangıç tabanı olarak koru (gecikmeli indekslemeye karşı)
      for (const localNote of notesList) {
        if (localNote && localNote.id && !deletedIdsSet.has(localNote.id) && localNote.dateKey === todayDateKey) {
          notesMap.set(localNote.id, { ...localNote });
        }
      }

      let lastEventTimeSec = 0;
      const lines = text.split('\n');
      for (const line of lines) {
        const trimmed = line.trim();
        if (!trimmed) continue;
        try {
          const envelope = JSON.parse(trimmed);
          if (envelope.time && envelope.time > lastEventTimeSec) {
            lastEventTimeSec = envelope.time;
          }
          if (envelope.event !== 'message' || !envelope.message) continue;
          const payload = JSON.parse(envelope.message);
          applySingleCloudPayload(payload, notesMap, likesByNote);
        } catch (_) {}
      }

      mergeAndCommitNotes(notesMap, likesByNote);
      initialLoaded = true;
      renderUI();

      // En son mesajın üzerinden 4 saatten fazla geçtiyse ve aktif not varsa TTL tazelemek için snapshot yayınla
      const nowSec = Math.floor(Date.now() / 1000);
      if (notesList.length > 0 && lastEventTimeSec > 0 && (nowSec - lastEventTimeSec) > 14400) {
        publishCloudEvent({ action: 'sync' });
      }
    } catch (err) {
      initialLoaded = true;
      renderUI();
    } finally {
      isSyncing = false;
    }
  }

  function connectRealtimeStream() {
    if (typeof EventSource === 'undefined') return;
    if (eventSource) {
      try { eventSource.close(); } catch (_) {}
      eventSource = null;
    }

    const topic = getTopicForDate(todayDateKey);
    const sseUrl = `${CLOUD_BASE_URL}/${encodeURIComponent(topic)}/sse`;

    try {
      const es = new EventSource(sseUrl);
      eventSource = es;

      es.onmessage = (e) => {
        if (!e || !e.data) return;
        try {
          const envelope = JSON.parse(e.data);
          if (envelope.event !== 'message' || !envelope.message) return;
          const payload = JSON.parse(envelope.message);

          checkDayRollover();
          const notesMap = new Map();
          for (const n of notesList) {
            if (n && n.id && !deletedIdsSet.has(n.id)) {
              notesMap.set(n.id, { ...n });
            }
          }
          const likesByNote = new Map();
          applySingleCloudPayload(payload, notesMap, likesByNote);

          // Tekil beğeni olayı geldiğinde sayacı güncelle
          if (payload.action === 'like' && payload.noteId) {
            const target = notesMap.get(payload.noteId);
            if (target) {
              const delta = payload.liked === false ? -1 : 1;
              if (payload.voterHash !== computeVoterHash(payload.noteId)) {
                target.likes = Math.max(0, (Number(target.likes) || 0) + delta);
              }
            }
          }

          mergeAndCommitNotes(notesMap);
          renderUI();
        } catch (_) {}
      };
    } catch (_) {}
  }

  /* ── GÜN SONU KONTROLÜ (00:00 SIFIRLAMA) ───────────────────── */
  function checkDayRollover(forcedTodayKey) {
    const actualToday = forcedTodayKey || getTodayDateKey();
    if (todayDateKey && actualToday !== todayDateKey) {
      todayDateKey = actualToday;
      notesList = [];
      deletedIdsSet = new Set();
      editingNoteId = null;
      cleanupLegacyAndExpiredStorage();
      saveLocalState();
      connectRealtimeStream();
      syncFromCloud();
      renderUI();
      return true;
    }
    if (!todayDateKey) {
      todayDateKey = actualToday;
    }
    return false;
  }

  /* ── NOT EKLEME / DÜZENLEME / SİLME / BEĞENME ──────────────── */
  function validateNoteInput(author, text) {
    const cleanAuthor = String(author || '').trim().slice(0, 30) || 'Anonim';
    const cleanText   = String(text || '').trim().slice(0, 220);

    if (!cleanText || cleanText.length < 2) {
      throw new Error('Lütfen en az 2 karakterden oluşan bir not yazın.');
    }
    return { cleanAuthor, cleanText };
  }

  function addQuote(author, text) {
    checkDayRollover();
    const { cleanAuthor, cleanText } = validateNoteInput(author, text);

    const now = new Date();
    const timeStr = now.toLocaleTimeString('tr-TR', {
      timeZone: 'Europe/Istanbul',
      hour: '2-digit',
      minute: '2-digit'
    });
    const noteId = `note_${Date.now()}_${Math.random().toString(36).substring(2, 8)}`;
    const ts = Date.now();

    const newNote = {
      id: noteId,
      dateKey: todayDateKey,
      author: cleanAuthor,
      text: cleanText,
      time: timeStr,
      createdAt: ts,
      updatedAt: ts,
      edited: false,
      likes: 0,
      ownerHash: computeOwnerHash(noteId)
    };

    notesList.unshift(newNote);
    addMyNoteId(noteId);
    setSavedAuthorName(cleanAuthor === 'Anonim' ? '' : cleanAuthor);
    saveLocalState();
    notifyOtherTabs();
    renderUI();

    publishCloudEvent({
      action: 'add',
      note: newNote
    });

    return newNote;
  }

  function editQuote(noteId, author, text) {
    checkDayRollover();
    const { cleanAuthor, cleanText } = validateNoteInput(author, text);

    const note = notesList.find(n => n.id === noteId);
    if (!note) {
      throw new Error('Düzenlenecek not bulunamadı.');
    }
    if (!isOwnNote(note)) {
      throw new Error('Yalnızca kendi yazdığınız notu düzenleyebilirsiniz.');
    }

    const ts = Date.now();
    note.author = cleanAuthor;
    note.text = cleanText;
    note.edited = true;
    note.updatedAt = ts;
    note.ownerHash = note.ownerHash || computeOwnerHash(noteId);

    setSavedAuthorName(cleanAuthor === 'Anonim' ? '' : cleanAuthor);
    saveLocalState();
    notifyOtherTabs();
    renderUI();

    publishCloudEvent({
      action: 'edit',
      noteId: note.id,
      ownerHash: note.ownerHash,
      author: note.author,
      text: note.text,
      updatedAt: ts
    });

    return note;
  }

  function deleteQuote(noteId) {
    checkDayRollover();
    const note = notesList.find(n => n.id === noteId);
    if (!note || !isOwnNote(note)) return false;

    const ownerHash = note.ownerHash || computeOwnerHash(noteId);
    deletedIdsSet.add(noteId);
    notesList = notesList.filter(n => n.id !== noteId);
    saveLocalState();
    notifyOtherTabs();
    renderUI();

    publishCloudEvent({
      action: 'delete',
      noteId,
      ownerHash,
      updatedAt: Date.now()
    });

    return true;
  }

  function toggleLikeQuote(noteId) {
    checkDayRollover();
    const note = notesList.find(n => n.id === noteId);
    if (!note) return null;

    const likedIds = getLikedNoteIds();
    const idx = likedIds.indexOf(noteId);
    let isLikedNow = false;

    if (idx === -1) {
      likedIds.push(noteId);
      note.likes = (Number(note.likes) || 0) + 1;
      isLikedNow = true;
    } else {
      likedIds.splice(idx, 1);
      note.likes = Math.max(0, (Number(note.likes) || 1) - 1);
      isLikedNow = false;
    }

    saveLikedNoteIds(likedIds);
    saveLocalState();
    notifyOtherTabs();
    renderUI();

    publishCloudEvent({
      action: 'like',
      noteId,
      voterHash: computeVoterHash(noteId),
      liked: isLikedNow
    });

    return { liked: isLikedNow, likes: note.likes };
  }

  /* ═══════════════════════════════════════════════════════════════
     RENDER — GÜNLÜK NOTLAR KARTI
     ═══════════════════════════════════════════════════════════════ */
  function renderUI() {
    const container = document.getElementById('daily-quote-card');
    if (!container) return;

    const likedList = getLikedNoteIds();
    const count = notesList.length;

    let bodyHTML = '';
    if (!initialLoaded && count === 0) {
      bodyHTML = `
        <div class="quote-empty">
          <p class="quote-empty-text">Günlük notlar yükleniyor...</p>
        </div>
      `;
    } else if (count === 0) {
      bodyHTML = `
        <div class="quote-empty">
          <p class="quote-empty-text">Bugün için henüz not bırakılmamış.</p>
          <p class="quote-empty-sub">Yazılan notlar siteye giren herkese görünür ve gün sonunda sıfırlanır.</p>
        </div>
      `;
    } else {
      bodyHTML = `
        <ul class="quote-list" aria-label="Bugün yazılan notlar">
          ${notesList.map(note => {
            const isLiked = likedList.includes(note.id);
            const mine = isOwnNote(note);
            const authorInitial = (note.author || 'A').charAt(0).toLocaleUpperCase('tr');
            const timeLabel = `${escapeHtml(note.time || '')}${note.edited ? ' · düzenlendi' : ''}`;

            return `
              <li class="quote-item ${mine ? 'quote-item--own' : ''}" data-note-id="${escapeHtml(note.id)}">
                <p class="quote-text">${escapeHtml(note.text)}</p>

                <div class="quote-footer">
                  <div class="quote-author-info">
                    <span class="quote-avatar" aria-hidden="true">${escapeHtml(authorInitial)}</span>
                    <div class="quote-author-details">
                      <div class="quote-author-row">
                        <span class="quote-author-name">${escapeHtml(note.author)}</span>
                        ${mine ? '<span class="quote-own-badge">Senin notun</span>' : ''}
                      </div>
                      <span class="quote-time">${timeLabel}</span>
                    </div>
                  </div>

                  <div class="quote-item-actions">
                    ${mine ? `
                      <button type="button" class="quote-action-btn quote-edit-btn" data-id="${escapeHtml(note.id)}" aria-label="Notu düzenle">
                        Düzenle
                      </button>
                      <button type="button" class="quote-action-btn quote-delete-btn" data-id="${escapeHtml(note.id)}" aria-label="Notu sil">
                        Sil
                      </button>
                    ` : ''}
                    <button type="button" class="quote-like-btn ${isLiked ? 'is-liked' : ''}" data-id="${escapeHtml(note.id)}" aria-label="Notu beğen" aria-pressed="${isLiked ? 'true' : 'false'}">
                      <span class="quote-like-icon" aria-hidden="true">${isLiked ? '♥' : '♡'}</span>
                      <span class="quote-like-count">${Number(note.likes) || 0}</span>
                    </button>
                  </div>
                </div>
              </li>
            `;
          }).join('')}
        </ul>
      `;
    }

    container.innerHTML = `
      <div class="quote-card-header">
        <div class="quote-header-left">
          <div class="quote-tag">
            <span class="quote-tag-text">Günlük Notlar${count > 0 ? ` (${count})` : ''}</span>
          </div>
          <span class="quote-reset-hint">Gün sonunda sıfırlanır</span>
        </div>
        <div class="quote-header-right">
          <button type="button" id="btn-open-quote-modal" class="quote-add-btn">
            + Not Yaz
          </button>
        </div>
      </div>

      ${bodyHTML}
    `;

    bindCardEvents(container);
  }

  function bindCardEvents(container) {
    const addBtn = container.querySelector('#btn-open-quote-modal');
    if (addBtn) {
      addBtn.addEventListener('click', () => openModalForCreate());
    }

    container.querySelectorAll('.quote-edit-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const noteId = btn.dataset.id;
        const note = notesList.find(n => n.id === noteId);
        if (note && isOwnNote(note)) {
          openModalForEdit(note);
        }
      });
    });

    container.querySelectorAll('.quote-delete-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const noteId = btn.dataset.id;
        if (deleteQuote(noteId)) {
          if (typeof haptic === 'function') haptic(15);
          if (typeof showToast === 'function') showToast('Notunuz silindi.');
        }
      });
    });

    container.querySelectorAll('.quote-like-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const noteId = btn.dataset.id;
        const res = toggleLikeQuote(noteId);
        if (res && typeof haptic === 'function') haptic(10);
      });
    });
  }

  /* ═══════════════════════════════════════════════════════════════
     NOT YAZMA & DÜZENLEME MODALI
     ═══════════════════════════════════════════════════════════════ */
  function hideFormError() {
    const errEl = document.getElementById('quote-form-error');
    if (errEl) {
      errEl.textContent = '';
      errEl.hidden = true;
    }
  }

  function showFormError(msg) {
    const errEl = document.getElementById('quote-form-error');
    if (errEl) {
      errEl.textContent = msg;
      errEl.hidden = false;
    }
  }

  function updateModalDateLabel() {
    const dateLabel = document.getElementById('quote-modal-date');
    if (!dateLabel) return;
    if (typeof describeDate === 'function' && todayDateKey) {
      const d = describeDate(todayDateKey);
      dateLabel.textContent = `${d.full} ${d.dayName} · Gün sonunda sıfırlanır`;
    } else {
      dateLabel.textContent = 'Bugünün Panosu · Gün sonunda sıfırlanır';
    }
  }

  function openModalForCreate() {
    const modal = document.getElementById('quote-modal');
    if (!modal) return;

    editingNoteId = null;
    hideFormError();

    const titleEl   = document.getElementById('quote-modal-title');
    const submitBtn = document.getElementById('quote-modal-submit');
    const nameInput = document.getElementById('quote-author-input');
    const textInput = document.getElementById('quote-text-input');
    const charCount = document.getElementById('quote-char-count');

    if (titleEl) titleEl.textContent = 'Günlük Not Yaz';
    if (submitBtn) submitBtn.textContent = 'Paylaş';
    if (nameInput) nameInput.value = getSavedAuthorName();
    if (textInput) textInput.value = '';
    if (charCount) charCount.textContent = '0 / 220';
    updateModalDateLabel();

    modal.showModal();
    if (nameInput && !nameInput.value) nameInput.focus();
    else if (textInput) textInput.focus();
  }

  function openModalForEdit(note) {
    const modal = document.getElementById('quote-modal');
    if (!modal || !note) return;

    editingNoteId = note.id;
    hideFormError();

    const titleEl   = document.getElementById('quote-modal-title');
    const submitBtn = document.getElementById('quote-modal-submit');
    const nameInput = document.getElementById('quote-author-input');
    const textInput = document.getElementById('quote-text-input');
    const charCount = document.getElementById('quote-char-count');

    if (titleEl) titleEl.textContent = 'Notu Düzenle';
    if (submitBtn) submitBtn.textContent = 'Kaydet';
    if (nameInput) nameInput.value = note.author === 'Anonim' ? '' : (note.author || '');
    if (textInput) textInput.value = note.text || '';
    if (charCount) charCount.textContent = `${(note.text || '').length} / 220`;
    updateModalDateLabel();

    modal.showModal();
    if (textInput) {
      textInput.focus();
      const len = textInput.value.length;
      try { textInput.setSelectionRange(len, len); } catch (_) {}
    }
  }

  function closeModal() {
    const modal = document.getElementById('quote-modal');
    editingNoteId = null;
    hideFormError();
    if (modal && modal.open) modal.close();
  }

  function initModal() {
    const modal     = document.getElementById('quote-modal');
    const form      = document.getElementById('quote-form');
    const closeBtn  = document.getElementById('quote-modal-close');
    const cancelBtn = document.getElementById('quote-modal-cancel');
    const textInput = document.getElementById('quote-text-input');
    const charCount = document.getElementById('quote-char-count');

    if (!modal) return;

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (cancelBtn) cancelBtn.addEventListener('click', closeModal);

    modal.addEventListener('click', (e) => {
      const rect = modal.getBoundingClientRect();
      const inBox = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
                     rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
      if (!inBox) closeModal();
    });

    if (textInput && charCount) {
      textInput.addEventListener('input', () => {
        hideFormError();
        charCount.textContent = `${textInput.value.length} / 220`;
      });
    }

    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        hideFormError();

        const author = document.getElementById('quote-author-input')?.value || '';
        const text   = document.getElementById('quote-text-input')?.value || '';

        try {
          if (editingNoteId) {
            editQuote(editingNoteId, author, text);
            closeModal();
            if (typeof showToast === 'function') showToast('✓ Notunuz güncellendi.');
          } else {
            addQuote(author, text);
            closeModal();
            if (typeof showToast === 'function') showToast('✓ Notunuz paylaşıldı.');
          }
          if (typeof haptic === 'function') haptic(20);
        } catch (err) {
          showFormError(err.message || 'Not kaydedilirken bir hata oluştu.');
        }
      });
    }
  }

  /* ── BAŞLATMA ──────────────────────────────────────────────── */
  function init(initialTodayKey) {
    todayDateKey = initialTodayKey || getTodayDateKey();
    loadLocalState();
    initModal();
    renderUI();

    // Sekmeler arası anlık senkronizasyon
    if (typeof BroadcastChannel !== 'undefined') {
      try {
        broadcastChan = new BroadcastChannel('yemekhane_daily_notes_v2');
        broadcastChan.onmessage = (e) => {
          if (e.data && e.data.type === 'notes_updated') {
            checkDayRollover();
            loadLocalState();
            renderUI();
          }
        };
      } catch (_) {}
    }

    // Buluttan mevcut günün notlarını çek ve canlı akışı başlat
    syncFromCloud();
    connectRealtimeStream();

    // Periyodik senkronizasyon ve gün sonu sıfırlama kontrolü
    clearInterval(pollTimer);
    pollTimer = setInterval(() => {
      checkDayRollover();
      if (!document.hidden) {
        syncFromCloud();
      }
    }, POLL_INTERVAL_MS);

    document.addEventListener('visibilitychange', () => {
      if (!document.hidden) {
        checkDayRollover();
        syncFromCloud();
      }
    });

    window.addEventListener('online', () => {
      checkDayRollover();
      syncFromCloud();
      connectRealtimeStream();
    });
  }

  function render() {
    checkDayRollover();
    renderUI();
  }

  function onDayChange(newTodayKey) {
    checkDayRollover(newTodayKey);
  }

  return {
    init,
    render,
    onDayChange,
    addQuote,
    editQuote,
    deleteQuote
  };

})();

window.QuoteManager = QuoteManager;
