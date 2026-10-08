/**
 * quoteManager.js — v1.0
 * ──────────────────────────────────────────────────────────────
 * Yemekhane Panosu — Günün Sözü & Öğrenci Köşesi Yönetimi
 *
 * Özellikler:
 *   • Tarih bazlı ("DD.MM.YYYY") söz saklama ve gösterim
 *   • Ziyaretçilerin isim ve günün sözü bırakabilmesi
 *   • O gün boyunca panoda kalma ve tarih değiştiğinde ilgili güne özel gösterim
 *   • Çoklu söz desteği (karusel / gezinme)
 *   • Beğeni (❤️) mekanizması ve yerel beğeni durumu hafızası
 *   • Ayın 31 günü için özenle seçilmiş ilham verici Türkçe varsayılan söz havuzu
 *   • localStorage kalıcılığı + gelecekteki bulut senkronizasyonu için modüler yapı
 */

'use strict';

const QuoteManager = (() => {

  const STORAGE_KEY = 'yemekhane_quotes_v1';
  const LIKES_KEY   = 'yemekhane_quote_likes_v1';
  const NAME_KEY    = 'yemekhane_user_author_name';

  /* ── 31 GÜN İÇİN İLHAM VERİCİ VARSAYILAN SÖZLER ──────────── */
  const DEFAULT_QUOTES = {
    1:  { author: "Cemal Süreya", text: "Yemek yemek üstüne ne düşünürsünüz bilmem ama kahvaltının mutlulukla bir ilgisi olmalı." },
    2:  { author: "Mevlana", text: "Güzel günler sana gelmez, sen onlara yürüyeceksin." },
    3:  { author: "Öğrenci Notu", text: "Zorlu derslerin ve vizelerin ilacı, dostlarla paylaşılan sıcak bir yemek masasıdır." },
    4:  { author: "Kampüs Bilgesi", text: "Sıcak bir çorba, serin bir sonbahar gününde en güzel terapidir." },
    5:  { author: "Anonim", text: "Pazartesi sendromuna karşı en güçlü kalkan: Yemekhanedeki güzel bir menü!" },
    6:  { author: "Nazım Hikmet", text: "Yüreğin kadar büyük, umudun kadar taze kal her yeni günde." },
    7:  { author: "Robert Collier", text: "Başarı, her gün bıkmadan usanmadan tekrarlanan küçük çabaların toplamıdır." },
    8:  { author: "Öğrenci Konseyi", text: "Bugün karnını doyururken ruhunu da güzel düşüncelerle ve motivasyonla besle." },
    9:  { author: "Can Yücel", text: "Ömür dediğin bir gündür, o da bugündür. Anın ve yemeğin tadını çıkar." },
    10: { author: "Kampüs Dostu", text: "Sınavlar gelir geçer, ama yemekhane sohbetleri ömür boyu unutulmaz." },
    11: { author: "Konfüçyüs", text: "Nereye giderseniz gidin, tüm kalbinizle gidin." },
    12: { author: "Ahmet Arif", text: "Terk etmedi sevdan beni, aç kaldım, susuz kaldım... Hayat paylaştıkça güzel." },
    13: { author: "Günün Hatırlatması", text: "Bol su içmeyi ve gün içinde kendine mola vermeyi unutma!" },
    14: { author: "Öğrenci Masası", text: "Tavuk pilav günleri kampüsün resmi bayramıdır!" },
    15: { author: "Seneca", text: "Hayat bir tiyatro sahnesidir; önemli olan ne kadar uzun olduğu değil, ne kadar iyi oynandığıdır." },
    16: { author: "Motivasyon Köşesi", text: "Gelecek, bugünden ona hazırlananlara aittir." },
    17: { author: "Anonim", text: "Bir tabak sıcak yemek, dertleri bir süreliğine unutturmaya yeter." },
    18: { author: "Cahit Sıtkı", text: "Memleket isterim; gök mavi, dal yeşil, tarla sarı olsun; kuşların çiçeklerin diyarı olsun." },
    19: { author: "Kampüs Ruhu", text: "Bugün kütüphaneye gitmeden önce yemekhaneye uğrayıp enerjini depola!" },
    20: { author: "Mevlana", text: "Dünle beraber gitti cancağızım, ne kadar söz varsa düne ait. Şimdi yeni şeyler söylemek lazım." },
    21: { author: "Öğrenci Fısıltısı", text: "Tatlı çıktığı günlerde tüm kampüsün yüzü gülüyor." },
    22: { author: "Albert Einstein", text: "Hayat bisiklet sürmek gibidir. Dengede kalmak için ilerlemeye devam etmelisiniz." },
    23: { author: "Günün Mottosu", text: "Bugün yapacağın küçük bir iyilik, birinin gününü tamamen aydınlatabilir." },
    24: { author: "Kampüs Aşçısı", text: "Yemeğin tuzu sevgidir; afiyet, sağlık ve neşe olsun!" },
    25: { author: "Özdemir Asaf", text: "Bana yalanlar söylese yetinecektim / Ama yalan söylediğini bilmeyecektim." },
    26: { author: "Öğrenci Notu", text: "Hafta sonu yaklaşıyor, son düzlükte enerjini yüksek tut!" },
    27: { author: "Atasözü", text: "Can boğazdan gelir, bugünün menüsü kaçmaz!" },
    28: { author: "Günün Dileği", text: "Sınavı olan herkese başarılar, dersi bitenlere huzurlu dinlenmeler." },
    29: { author: "Mustafa Kemal Atatürk", text: "Geleceğin ışığı sizlersiniz; çalışmak, daima çalışmak ve başarmak gerek." },
    30: { author: "Cumhuriyet Ruhu", text: "Nice bayramlara, aydınlık yarınlara ve birlik içinde güzel günlere!" },
    31: { author: "Ekim Vedası", text: "Bir ayı daha geride bırakırken biriktirdiğimiz güzel anılara ve dostluklara şerefe." }
  };

  /* ── DURUM ─────────────────────────────────────────────────── */
  let activeIndex = 0;       // O gün birden fazla söz varsa hangisinin gösterildiği
  let currentDateKey = '';

  /* ── YARDIMCILAR ───────────────────────────────────────────── */
  function getStoredQuotes() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : {};
    } catch (_) {
      return {};
    }
  }

  function saveStoredQuotes(data) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (e) {
      console.warn('[QuoteManager] Kayıt başarısız:', e);
    }
  }

  function getLikedQuoteIds() {
    try {
      const raw = localStorage.getItem(LIKES_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (_) {
      return [];
    }
  }

  function setLikedQuoteId(id) {
    const list = getLikedQuoteIds();
    if (!list.includes(id)) {
      list.push(id);
      try {
        localStorage.setItem(LIKES_KEY, JSON.stringify(list));
      } catch (_) {}
    }
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

  /**
   * Belirli bir tarih ("DD.MM.YYYY") için söz listesini döndürür.
   * Kullanıcı sözleri + varsayılan gün sözü.
   */
  function getQuotesForDate(dateKey) {
    const stored = getStoredQuotes();
    const userQuotes = Array.isArray(stored[dateKey]) ? stored[dateKey] : [];

    // Günün gün numarasına göre varsayılan sözü bul (örn: "06.10.2026" -> 6)
    const dayNum = parseInt(dateKey.split('.')[0], 10) || 1;
    const def = DEFAULT_QUOTES[dayNum] || DEFAULT_QUOTES[1];

    const defaultQuoteObj = {
      id: `default_${dateKey}`,
      author: def.author,
      text: def.text,
      time: 'Günün Sözü',
      likes: 5,
      isDefault: true
    };

    // Eğer kullanıcı sözü varsa kullanıcı sözlerini öne koy, ardından varsayılanı göster
    if (userQuotes.length > 0) {
      return [...userQuotes, defaultQuoteObj];
    }
    return [defaultQuoteObj];
  }

  /**
   * Yeni söz ekler.
   */
  function addQuote(dateKey, author, text) {
    const cleanAuthor = String(author || '').trim() || 'Anonim Öğrenci';
    const cleanText   = String(text || '').trim();

    if (!cleanText || cleanText.length < 3) {
      throw new Error('Lütfen en az 3 karakterden oluşan bir söz yazın.');
    }

    const now = new Date();
    const timeStr = now.toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' });

    const newQuote = {
      id: `quote_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`,
      author: cleanAuthor,
      text: cleanText,
      time: timeStr,
      likes: 1,
      isDefault: false
    };

    const stored = getStoredQuotes();
    if (!Array.isArray(stored[dateKey])) {
      stored[dateKey] = [];
    }
    // En başa ekle (en yeni söz ilk görünsün)
    stored[dateKey].unshift(newQuote);
    saveStoredQuotes(stored);
    setSavedAuthorName(cleanAuthor);

    // Kendi sözünü otomatik beğenmiş say
    setLikedQuoteId(newQuote.id);

    return newQuote;
  }

  /**
   * Söz beğenisini artırır.
   */
  function likeQuote(dateKey, quoteId) {
    const likedList = getLikedQuoteIds();
    if (likedList.includes(quoteId)) {
      return { alreadyLiked: true };
    }

    const stored = getStoredQuotes();
    const quotes = stored[dateKey] || [];
    const quote = quotes.find(q => q.id === quoteId);

    if (quote) {
      quote.likes = (quote.likes || 0) + 1;
      saveStoredQuotes(stored);
    }
    setLikedQuoteId(quoteId);

    return { alreadyLiked: false, newLikes: quote ? quote.likes : null };
  }

  /* ═══════════════════════════════════════════════════════════════
     RENDER — GÜNÜN SÖZÜ KARTI
     ═══════════════════════════════════════════════════════════════ */
  function render(dateKey) {
    currentDateKey = dateKey;
    const container = document.getElementById('daily-quote-card');
    if (!container) return;

    const quotes = getQuotesForDate(dateKey);
    if (activeIndex >= quotes.length) activeIndex = 0;
    if (activeIndex < 0) activeIndex = quotes.length - 1;

    const quote = quotes[activeIndex];
    const likedList = getLikedQuoteIds();
    const isLiked = likedList.includes(quote.id);
    const authorInitial = (quote.author || 'A').charAt(0).toLocaleUpperCase('tr');

    const total = quotes.length;
    const navHTML = total > 1 ? `
      <div class="quote-nav" aria-label="Söz gezintisi">
        <button type="button" class="quote-nav-btn quote-prev" aria-label="Önceki söz">‹</button>
        <span class="quote-counter">${activeIndex + 1} / ${total}</span>
        <button type="button" class="quote-nav-btn quote-next" aria-label="Sonraki söz">›</button>
      </div>
    ` : '';

    container.innerHTML = `
      <div class="quote-card-header">
        <div class="quote-tag">
          <span class="quote-tag-icon" aria-hidden="true">💬</span>
          <span class="quote-tag-text">${quote.isDefault ? 'Günün Sözü & İlhamı' : 'Öğrenci Köşesi · Günün Sözü'}</span>
        </div>
        <div class="quote-header-right">
          ${navHTML}
          <button type="button" id="btn-open-quote-modal" class="quote-add-btn">
            <span aria-hidden="true">✍️</span> Söz Bırak
          </button>
        </div>
      </div>

      <div class="quote-content">
        <p class="quote-text">“${escapeHtml(quote.text)}”</p>
      </div>

      <div class="quote-footer">
        <div class="quote-author-info">
          <span class="quote-avatar" aria-hidden="true">${escapeHtml(authorInitial)}</span>
          <div class="quote-author-details">
            <span class="quote-author-name">${escapeHtml(quote.author)}</span>
            <span class="quote-time">${escapeHtml(quote.time)}</span>
          </div>
        </div>

        <button type="button" class="quote-like-btn ${isLiked ? 'is-liked' : ''}" data-id="${quote.id}" aria-label="Sözü beğen">
          <span class="quote-like-icon" aria-hidden="true">${isLiked ? '❤️' : '🤍'}</span>
          <span class="quote-like-count">${quote.likes || 1}</span>
        </button>
      </div>
    `;

    bindCardEvents(container, dateKey, quote);
  }

  function bindCardEvents(container, dateKey, quote) {
    // Söz Bırak butonu
    const addBtn = container.querySelector('#btn-open-quote-modal');
    if (addBtn) {
      addBtn.addEventListener('click', () => openModal(dateKey));
    }

    // Karusel gezintisi
    const prevBtn = container.querySelector('.quote-prev');
    const nextBtn = container.querySelector('.quote-next');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        activeIndex--;
        render(dateKey);
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        activeIndex++;
        render(dateKey);
      });
    }

    // Beğeni butonu
    const likeBtn = container.querySelector('.quote-like-btn');
    if (likeBtn) {
      likeBtn.addEventListener('click', () => {
        const result = likeQuote(dateKey, quote.id);
        if (!result.alreadyLiked) {
          if (typeof haptic === 'function') haptic(15);
          render(dateKey);
          if (typeof showToast === 'function') showToast('❤️ Beğenildi!');
        } else {
          if (typeof showToast === 'function') showToast('Bu sözü zaten beğendiniz.');
        }
      });
    }
  }

  /* ═══════════════════════════════════════════════════════════════
     SÖZ BIRAKMA MODALI
     ═══════════════════════════════════════════════════════════════ */
  function openModal(dateKey) {
    const modal = document.getElementById('quote-modal');
    if (!modal) return;

    const nameInput = document.getElementById('quote-author-input');
    const textInput = document.getElementById('quote-text-input');
    const charCount = document.getElementById('quote-char-count');
    const dateLabel = document.getElementById('quote-modal-date');

    if (nameInput) nameInput.value = getSavedAuthorName();
    if (textInput) textInput.value = '';
    if (charCount) charCount.textContent = '0 / 220';
    if (dateLabel && typeof describeDate === 'function') {
      const d = describeDate(dateKey);
      dateLabel.textContent = `${d.full} ${d.dayName} Panosu`;
    }

    modal.showModal();
    if (nameInput && !nameInput.value) nameInput.focus();
    else if (textInput) textInput.focus();
  }

  function closeModal() {
    const modal = document.getElementById('quote-modal');
    if (modal) modal.close();
  }

  function initModal() {
    const modal = document.getElementById('quote-modal');
    const form  = document.getElementById('quote-form');
    const closeBtn = document.getElementById('quote-modal-close');
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
        const len = textInput.value.length;
        charCount.textContent = `${len} / 220`;
      });
    }

    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const author = document.getElementById('quote-author-input')?.value || '';
        const text   = document.getElementById('quote-text-input')?.value || '';

        try {
          addQuote(currentDateKey, author, text);
          activeIndex = 0; // Yeni eklenen söz en başta görünsün
          closeModal();
          render(currentDateKey);
          if (typeof showToast === 'function') showToast('✓ Günün sözü panoya eklendi!');
          if (typeof haptic === 'function') haptic(25);
        } catch (err) {
          alert(err.message || 'Söz eklenirken bir hata oluştu.');
        }
      });
    }
  }

  /* ── BAŞLATMA ──────────────────────────────────────────────── */
  function init() {
    initModal();
  }

  return {
    init,
    render,
    getQuotesForDate,
    addQuote,
    likeQuote
  };

})();

window.QuoteManager = QuoteManager;
