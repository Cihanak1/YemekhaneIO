/**
 * app.js  — v4.2
 * ──────────────────────────────────────────────────────────────
 * Günlük Menü Panosu — Ana Uygulama Mantığı
 *
 * v4.2:
 *   • Mobil Öğün Filtreleme (Tümü | Kahvaltı | Akşam) + saat bazlı akıllı başlangıç
 *   • Hızlı Takvim Seçici (Doğrudan istenen güne 1 tıkla atlama)
 *   • Menüyü Paylaş / Kopyala (Web Share API + Pano kopyalama + Toast)
 *   • Ay İçi Anlık Yemek Arama (In-memory hızlı yemek bulucu ve güne atlama)
 *   • PWA Service Worker & Çevrimdışı Çalışma Desteği
 *   • Klavye kısayolları (← →, T, Ctrl+K / / arama)
 *   • Titreşim / Haptik geribildirim (destekleyen mobil cihazlar için)
 */

'use strict';

/* ── CONFIG ─────────────────────────────────────────────────── */
const CONFIG = {
  morningFile:    'data/sabah_kahvaltisi.json',
  eveningFile:    'data/aksam_yemegi.json',
  timeZone:       'Europe/Istanbul',
  swipeThreshold: 55,   // px
};

const DAY_NAMES  = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];
const DAY_SHORT  = ['Paz', 'Pzt', 'Sal', 'Çar', 'Per', 'Cum', 'Cmt'];
const MONTHS     = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran',
                    'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];

/* Akşam yemeği "N. Yemek Çeşitleri" → görünen kategori */
const DINNER_CATEGORIES = { 1: 'Çorba', 2: 'Ana Yemek', 3: 'Pilav / Makarna', 4: 'Tamamlayıcı' };
const DINNER_FALLBACK_ICONS = { 1: '🍲', 2: '🍛', 3: '🍚', 4: '🥗' };

/* İsimden emoji seçimi (tr küçük harf üzerinde, sıralama önemli) */
const ICON_RULES = [
  [/çorba|aşı/,                                             '🍲'],
  [/yumurta|omlet|menemen/,                                 '🍳'],
  [/köfte|kebab|kebap|kavurma|döner|tavuk|şinitzel|biftek|tantuni|burger|nugget|şiş|güveç|külbastı|tava/, '🍗'],
  [/pizza/,                                                 '🍕'],
  [/sosis|sucuk/,                                           '🌭'],
  [/kızartma/,                                              '🍟'],
  [/patates/,                                               '🥔'],
  [/peynir|labne/,                                          '🧀'],
  [/zeytin/,                                                '🫒'],
  [/simit|poğaça|açma|börek|ekmek/,                         '🥐'],
  [/kek|browni|revani|baklava|şekerpare|tulumba|puding|sütlaç|sultan|helva/, '🍰'],
  [/reçel|bal|çikolata/,                                    '🍯'],
  [/pilav|bulgur/,                                          '🍚'],
  [/makarna|erişte|mantı/,                                  '🍝'],
  [/salata|cacık|haydari|ezme|tarator/,                     '🥗'],
  [/ayran|yoğurt/,                                          '🥛'],
  [/fasülye|nohut|bezelye|ıspanak|türlü|musakka|karnıyarık|kalye|imam|mücver|graten|kabak|dolma/, '🥘'],
];

const EXTRA_ICONS = [[/ekmek/, '🍞'], [/su$/, '💧'], [/çay/, '🍵']];

/* ── STATE ───────────────────────────────────────────────────── */
const state = {
  today:      '',
  selected:   '',
  mealFilter: 'all',   // 'all' | 'morning' | 'evening'
  dates:      [],      // menüsü olan günler (sıralı "DD.MM.YYYY")
  min:        0,       // gezinme sınırları (UTC ms)
  max:        0,
  sources:    { morning: null, evening: null },
  errors:     { morning: null, evening: null },
};

let clockTimer = null;
let toastTimer = null;
const chipByDate = new Map();

/* ── DOM HELPERS ─────────────────────────────────────────────── */
const $ = (id) => document.getElementById(id);

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

const prefersReducedMotion = () =>
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function haptic(ms = 10) {
  if (navigator.vibrate) {
    try { navigator.vibrate(ms); } catch (_) {}
  }
}

function showToast(message) {
  const t = $('toast');
  if (!t) return;
  t.textContent = message;
  t.hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { t.hidden = true; }, 2600);
}

/* ── TARİH YARDIMCILARI ("DD.MM.YYYY" anahtarları) ──────────── */
const pad2 = (n) => String(n).padStart(2, '0');
const DAY_MS = 86400000;

function keyToUTC(key) {
  const [d, m, y] = key.split('.').map(Number);
  return Date.UTC(y, m - 1, d);
}

function utcToKey(ms) {
  const dt = new Date(ms);
  return `${pad2(dt.getUTCDate())}.${pad2(dt.getUTCMonth() + 1)}.${dt.getUTCFullYear()}`;
}

function keyToISO(key) {
  const [d, m, y] = key.split('.');
  return `${y}-${m}-${d}`;
}

function isoToKey(iso) {
  const [y, m, d] = iso.split('-');
  return `${d}.${m}.${y}`;
}

const addDays = (key, n) => utcToKey(keyToUTC(key) + n * DAY_MS);

function describeDate(key) {
  const dt = new Date(keyToUTC(key));
  const wd = dt.getUTCDay();
  return {
    dayName: DAY_NAMES[wd],
    short:   DAY_SHORT[wd],
    dayNum:  dt.getUTCDate(),
    full:    `${dt.getUTCDate()} ${MONTHS[dt.getUTCMonth()]} ${dt.getUTCFullYear()}`,
    weekend: wd === 0 || wd === 6,
  };
}

/* Intl biçimlendiricileri */
const dateFmt = new Intl.DateTimeFormat('en-GB', {
  timeZone: CONFIG.timeZone, day: '2-digit', month: '2-digit', year: 'numeric',
});
const timeFmt = new Intl.DateTimeFormat('tr-TR', {
  timeZone: CONFIG.timeZone, hour: '2-digit', minute: '2-digit', second: '2-digit', hourCycle: 'h23',
});

function todayKey(now = new Date()) {
  const p = {};
  for (const { type, value } of dateFmt.formatToParts(now)) p[type] = value;
  return `${p.day}.${p.month}.${p.year}`;
}

/* ── İKON SEÇİMİ ─────────────────────────────────────────────── */
function pickIcon(name, kind, catNum) {
  const s = name.toLocaleLowerCase('tr');
  for (const [re, icon] of ICON_RULES) if (re.test(s)) return icon;
  if (kind === 'evening' && DINNER_FALLBACK_ICONS[catNum]) return DINNER_FALLBACK_ICONS[catNum];
  return '🍽️';
}

function extraIcon(name) {
  const s = name.toLocaleLowerCase('tr');
  for (const [re, icon] of EXTRA_ICONS) if (re.test(s)) return icon;
  return '•';
}

/* ═══════════════════════════════════════════════════════════════
   RENDER — KARTLAR
   ═══════════════════════════════════════════════════════════════ */
function foodItemHTML(item, i, kind) {
  const clean   = item.name.replace(/^\*+\s*/, '').trim();
  const options = kind === 'evening'
    ? clean.split(/\s*\/+\s*/).filter(Boolean)
    : [clean];

  const catNum = Number((item.kategori.match(/^(\d)/) || [])[1]) || 0;
  const cat    = kind === 'evening' ? (DINNER_CATEGORIES[catNum] || '') : '';
  const icon   = pickIcon(options[0] || clean, kind, catNum);

  const catLabel = cat
    ? `${cat}${options.length > 1 ? ` · ${options.length} seçenek` : ''}`
    : (options.length > 1 ? `${options.length} seçenek` : '');

  const nameHTML = options.length > 1
    ? `<ul class="food-options" aria-label="Seçenekler">${
        options.map(o => `<li class="food-option">${escapeHtml(o)}</li>`).join('')
      }</ul>`
    : `<span class="food-name">${escapeHtml(options[0] || clean)}</span>`;

  return `<li class="food-item" style="--i:${i}">` +
      `<span class="food-icon" aria-hidden="true">${icon}</span>` +
      `<div class="food-body">` +
        (catLabel ? `<span class="food-cat">${escapeHtml(catLabel)}</span>` : '') +
        nameHTML +
        (item.gramaj ? `<span class="food-gram">${escapeHtml(item.gramaj)}</span>` : '') +
      `</div>` +
    `</li>`;
}

function emptyHTML(icon, title, desc) {
  return `<div class="card-empty">` +
      `<span class="card-empty-icon" aria-hidden="true">${icon}</span>` +
      `<p class="card-empty-title">${escapeHtml(title)}</p>` +
      `<p class="card-empty-desc">${escapeHtml(desc)}</p>` +
    `</div>`;
}

function renderCard(kind) {
  const isMorning = kind === 'morning';
  const bodyEl    = $(`card-${kind}-body`);
  const metaEl    = $(`${kind}-meta`);
  const extrasEl  = $(`${kind}-extras`);
  const source    = state.sources[kind];
  const mealName  = isMorning ? 'Sabah kahvaltısı' : 'Akşam yemeği';

  if (!bodyEl) return;

  bodyEl.removeAttribute('aria-busy');
  metaEl.textContent = '';
  extrasEl.hidden = true;

  if (!source) {
    bodyEl.innerHTML = emptyHTML('⚠️', `${mealName} yüklenemedi`,
      state.errors[kind] || 'Menü verisi okunamadı.');
    return;
  }

  const menu = source.getDay(state.selected);
  if (!menu || menu.items.length === 0) {
    const d = describeDate(state.selected);
    bodyEl.innerHTML = emptyHTML(isMorning ? '☀️' : '🌙', `${mealName} menüsü yok`,
      `${d.full} ${d.dayName} için menü girilmemiştir.`);
    return;
  }

  bodyEl.innerHTML = `<ol class="food-list">${
    menu.items.map((it, i) => foodItemHTML(it, i, kind)).join('')
  }</ol>`;

  metaEl.textContent = menu.calories
    ? `🔥 ${Number(menu.calories).toLocaleString('tr-TR')} kcal`
    : `${menu.items.length} çeşit`;

  if (menu.extras && menu.extras.length) {
    extrasEl.innerHTML = `<span class="extras-label">Yanında</span>` +
      menu.extras.map(x =>
        `<span class="extra-chip">${extraIcon(x)} ${escapeHtml(x)}</span>`).join('');
    extrasEl.hidden = false;
  }
}

/* ═══════════════════════════════════════════════════════════════
   RENDER — BAŞLIK & GÜN ŞERİDİ
   ═══════════════════════════════════════════════════════════════ */
function renderHeader() {
  const d       = describeDate(state.selected);
  const isToday = state.selected === state.today;
  const cur     = keyToUTC(state.selected);

  $('header-date').textContent = d.full;
  $('header-day').textContent  = d.dayName;
  $('today-pill').hidden = !isToday;
  $('today-btn').hidden  = isToday;
  $('prev-day').disabled = cur <= state.min;
  $('next-day').disabled = cur >= state.max;

  // Gizli tarih seçici girdisini eşitle
  const datePicker = $('date-picker-input');
  if (datePicker) {
    datePicker.value = keyToISO(state.selected);
  }

  document.title = `${d.full} ${d.dayName} | Günlük Yemek Menüsü`;
}

function buildStrip() {
  const strip = $('day-strip');
  const list  = $('day-strip-list');
  chipByDate.clear();

  if (state.dates.length === 0) {
    strip.hidden = true;
    return;
  }

  list.innerHTML = state.dates.map(key => {
    const d = describeDate(key);
    return `<li><button type="button" class="day-chip${d.weekend ? ' is-weekend' : ''}"` +
      ` data-date="${key}" aria-pressed="false" aria-label="${d.full}, ${d.dayName}"` +
      `${key === state.today ? ' aria-current="date"' : ''}>` +
      `<span class="day-chip-wd">${d.short}</span>` +
      `<span class="day-chip-num">${d.dayNum}</span>` +
      `</button></li>`;
  }).join('');

  list.querySelectorAll('.day-chip').forEach(btn => chipByDate.set(btn.dataset.date, btn));
  strip.hidden = false;
}

function updateStrip(smooth) {
  const strip = $('day-strip');
  for (const [key, btn] of chipByDate) {
    btn.setAttribute('aria-pressed', key === state.selected ? 'true' : 'false');
  }
  const active = chipByDate.get(state.selected);
  if (!active || strip.hidden) return;

  const left = active.offsetLeft - (strip.clientWidth - active.offsetWidth) / 2;
  strip.scrollTo({ left, behavior: smooth && !prefersReducedMotion() ? 'smooth' : 'auto' });
}

/* ═══════════════════════════════════════════════════════════════
   ÖĞÜN FİLTRELEME (MOBİL SEKMELERİ)
   ═══════════════════════════════════════════════════════════════ */
function setMealFilter(filter) {
  state.mealFilter = filter;
  const grid = $('menu-grid');
  if (grid) {
    grid.dataset.filter = filter;
  }

  const buttons = document.querySelectorAll('.meal-switch-btn');
  buttons.forEach(btn => {
    const active = btn.dataset.meal === filter;
    btn.classList.toggle('is-active', active);
    btn.setAttribute('aria-selected', active ? 'true' : 'false');
  });
}

function render(smooth = true) {
  renderHeader();
  updateStrip(smooth);
  renderCard('morning');
  renderCard('evening');
  if (window.QuoteManager) {
    QuoteManager.render(state.today);
  }
}

/* ── NOTLAR ──────────────────────────────────────────────────── */
function renderNotes() {
  const groups = [];
  const sign   = state.sources.morning?.signature || state.sources.evening?.signature;

  [['morning', 'Kahvaltı'], ['evening', 'Akşam Yemeği']].forEach(([kind, label]) => {
    const notes = state.sources[kind]?.notes || [];
    if (!notes.length) return;
    groups.push(
      `<section class="notes-group notes-group--${kind}"><h3>${label}</h3><ul>${
        notes.map(n => `<li>${escapeHtml(n)}</li>`).join('')
      }</ul></section>`);
  });

  if (!groups.length) return;
  if (sign?.isim) {
    groups.push(`<p class="notes-sign">Onaylayan: ${escapeHtml(sign.isim)}${
      sign.unvan ? ` — ${escapeHtml(sign.unvan)}` : ''}</p>`);
  }
  $('notes-body').innerHTML = groups.join('');
  $('notes').hidden = false;
}

/* ── HATA ────────────────────────────────────────────────────── */
function showError(messages) {
  $('error-container').innerHTML =
    `<div class="error-banner"><span class="error-banner-icon" aria-hidden="true">⚠️</span>` +
    `<span class="error-banner-text">${messages.map(escapeHtml).join('<br>')}</span></div>`;
}

/* ═══════════════════════════════════════════════════════════════
   GEZİNME
   ═══════════════════════════════════════════════════════════════ */
function recomputeBounds() {
  if (state.dates.length === 0) return;
  const all = state.dates.map(keyToUTC);
  state.min = Math.min(...all);
  state.max = Math.max(...all);
}

function selectDate(key, smooth = true) {
  const t = keyToUTC(key);
  if (t < state.min || t > state.max || key === state.selected) return;
  haptic(10);
  state.selected = key;
  render(smooth);
}

const go = (delta) => selectDate(addDays(state.selected, delta));

/* ═══════════════════════════════════════════════════════════════
   PAYLAŞIM / KOPYALAMA
   ═══════════════════════════════════════════════════════════════ */
async function shareOrCopyMenu() {
  const d = describeDate(state.selected);
  const mMenu = state.sources.morning?.getDay(state.selected);
  const eMenu = state.sources.evening?.getDay(state.selected);

  let text = `🍽️ ${d.full} ${d.dayName} Yemek Menüsü\n\n`;

  if (mMenu && mMenu.items.length) {
    text += `☀️ Sabah Kahvaltısı:\n`;
    mMenu.items.forEach(it => {
      text += `• ${it.name}${it.gramaj ? ` (${it.gramaj})` : ''}\n`;
    });
    if (mMenu.extras?.length) {
      text += `  (Yanında: ${mMenu.extras.join(', ')})\n`;
    }
    text += '\n';
  }

  if (eMenu && eMenu.items.length) {
    text += `🌙 Akşam Yemeği:\n`;
    eMenu.items.forEach(it => {
      text += `• ${it.name}${it.gramaj ? ` (${it.gramaj})` : ''}\n`;
    });
    if (eMenu.extras?.length) {
      text += `  (Yanında: ${eMenu.extras.join(', ')})\n`;
    }
  }

  const shareData = {
    title: `${d.full} ${d.dayName} Yemek Menüsü`,
    text: text.trim(),
  };

  // Web Share API (özellikle mobilde WhatsApp/Telegram paylaşımı)
  if (navigator.share && navigator.canShare && navigator.canShare(shareData)) {
    try {
      await navigator.share(shareData);
      return;
    } catch (err) {
      if (err.name === 'AbortError') return;
    }
  }

  // Pano Kopyalama Fallback'i
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      await navigator.clipboard.writeText(text.trim());
    } else {
      const ta = document.createElement('textarea');
      ta.value = text.trim();
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
    }
    showToast('✓ Menü panoya kopyalandı!');
    haptic(15);
  } catch (err) {
    console.error('Kopyalama başarısız', err);
    showToast('Menü kopyalanamadı.');
  }
}

/* ═══════════════════════════════════════════════════════════════
   AY İÇİ ANLIK ARAMA (SEARCH MODAL)
   ═══════════════════════════════════════════════════════════════ */
const TR_CHAR_MAP = {
  i: '[iıİI]', ı: '[iıİI]', İ: '[iıİI]', I: '[iıİI]',
  s: '[sşSŞ]', ş: '[sşSŞ]', S: '[sşSŞ]', Ş: '[sşSŞ]',
  c: '[cçCÇ]', ç: '[cçCÇ]', C: '[cçCÇ]', Ç: '[cçCÇ]',
  g: '[gğGĞ]', ğ: '[gğGĞ]', G: '[gğGĞ]', Ğ: '[gğGĞ]',
  u: '[uüUÜ]', ü: '[uüUÜ]', U: '[uüUÜ]', Ü: '[uüUÜ]',
  o: '[oöOÖ]', ö: '[oöOÖ]', O: '[oöOÖ]', Ö: '[oöOÖ]',
};

function buildTurkishRegex(query, global = false) {
  const pattern = Array.from(query).map(ch => TR_CHAR_MAP[ch] || escapeRegex(ch)).join('');
  return new RegExp(`(${pattern})`, global ? 'gi' : 'i');
}

function highlightTurkishMatch(text, regex) {
  const str = String(text || '');
  let result = '';
  let lastIndex = 0;
  regex.lastIndex = 0;
  let match;

  while ((match = regex.exec(str)) !== null) {
    if (match[0].length === 0) {
      regex.lastIndex++;
      continue;
    }
    result += escapeHtml(str.slice(lastIndex, match.index));
    result += `<mark>${escapeHtml(match[0])}</mark>`;
    lastIndex = match.index + match[0].length;
    if (!regex.global) break;
  }
  result += escapeHtml(str.slice(lastIndex));
  return result;
}

function setupSearch() {
  const modal      = $('search-modal');
  const input      = $('search-input');
  const resultsEl  = $('search-results');
  const statusEl   = $('search-status');
  const closeBtn   = $('search-close');
  const searchBtn  = $('btn-search');

  if (!modal || !searchBtn) return;

  function openModal() {
    modal.showModal();
    input.value = '';
    renderSearchResults('');
    input.focus();
  }

  function closeModal() {
    modal.close();
  }

  function activateResultItem(item) {
    if (!item) return;
    const dateKey = item.dataset.date;
    const meal    = item.dataset.meal;

    closeModal();
    if (dateKey) selectDate(dateKey);
    if (meal && window.innerWidth < 860) setMealFilter(meal);
  }

  searchBtn.addEventListener('click', openModal);
  if (closeBtn) closeBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    // Backdrop tıklaması ile kapat
    const rect = modal.getBoundingClientRect();
    const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
                        rect.left <= e.clientX && e.clientX <= rect.left + rect.width);
    if (!isInDialog) closeModal();
  });

  input.addEventListener('input', (e) => {
    renderSearchResults(e.target.value.trim());
  });

  input.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown') {
      const first = resultsEl.querySelector('.search-result-item');
      if (first) {
        e.preventDefault();
        first.focus();
      }
    } else if (e.key === 'Enter') {
      const first = resultsEl.querySelector('.search-result-item');
      if (first) {
        e.preventDefault();
        activateResultItem(first);
      }
    }
  });

  resultsEl.addEventListener('click', (e) => {
    const item = e.target.closest('.search-result-item');
    if (item) activateResultItem(item);
  });

  resultsEl.addEventListener('keydown', (e) => {
    const item = e.target.closest('.search-result-item');
    if (!item) return;

    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      activateResultItem(item);
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      const next = item.nextElementSibling;
      if (next) next.focus();
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      const prev = item.previousElementSibling;
      if (prev) prev.focus();
      else input.focus();
    }
  });

  function renderSearchResults(query) {
    if (!query) {
      statusEl.textContent = 'Aramak istediğiniz yemeği yazın...';
      resultsEl.innerHTML = '';
      return;
    }

    const matchRegex = buildTurkishRegex(query, false);
    const highlightRegex = buildTurkishRegex(query, true);
    const matches = [];

    state.dates.forEach(dateKey => {
      const d = describeDate(dateKey);

      // Sabah
      const mMenu = state.sources.morning?.getDay(dateKey);
      if (mMenu) {
        mMenu.items.forEach(it => {
          if (matchRegex.test(it.name)) {
            matches.push({ dateKey, dateInfo: d, meal: 'morning', mealLabel: '☀️ Sabah', item: it });
          }
        });
      }

      // Akşam
      const eMenu = state.sources.evening?.getDay(dateKey);
      if (eMenu) {
        eMenu.items.forEach(it => {
          if (matchRegex.test(it.name)) {
            matches.push({ dateKey, dateInfo: d, meal: 'evening', mealLabel: '🌙 Akşam', item: it });
          }
        });
      }
    });

    if (matches.length === 0) {
      statusEl.textContent = `"${query}" ile eşleşen yemek bulunamadı.`;
      resultsEl.innerHTML = '';
      return;
    }

    statusEl.textContent = `${matches.length} sonuç bulundu:`;

    resultsEl.innerHTML = matches.map(m => {
      const highlighted = highlightTurkishMatch(m.item.name, highlightRegex);
      return `<li class="search-result-item search-result-item--${m.meal}" data-date="${m.dateKey}" data-meal="${m.meal}" tabindex="0" role="option">` +
        `<div class="search-item-info">` +
          `<span class="search-item-dish">${highlighted}</span>` +
          `<span class="search-item-meta">${m.mealLabel}${m.item.gramaj ? ` · ${escapeHtml(m.item.gramaj)}` : ''}</span>` +
        `</div>` +
        `<span class="search-item-date-badge">${m.dateInfo.dayNum} ${m.dateInfo.short}</span>` +
      `</li>`;
    }).join('');
  }
}

function escapeRegex(s) {
  return s.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&');
}

/* ═══════════════════════════════════════════════════════════════
   ETKİNLİKLER VE BAĞLANTILAR
   ═══════════════════════════════════════════════════════════════ */
function bindEvents() {
  $('prev-day').addEventListener('click', () => go(-1));
  $('next-day').addEventListener('click', () => go(1));
  $('today-btn').addEventListener('click', () => selectDate(state.today));

  // Gün şeridi seçimi
  $('day-strip-list').addEventListener('click', (e) => {
    const btn = e.target.closest('.day-chip');
    if (btn) selectDate(btn.dataset.date);
  });

  // Öğün filtre sekmeleri
  const mealSwitch = $('meal-switch');
  if (mealSwitch) {
    mealSwitch.addEventListener('click', (e) => {
      const btn = e.target.closest('.meal-switch-btn');
      if (btn && btn.dataset.meal) {
        haptic(8);
        setMealFilter(btn.dataset.meal);
      }
    });
  }

  // Paylaş / Kopyala butonu
  const shareBtn = $('btn-share');
  if (shareBtn) {
    shareBtn.addEventListener('click', shareOrCopyMenu);
  }

  // Takvim butonu & Yerel Tarih Seçici
  const calBtn = $('btn-calendar');
  const datePicker = $('date-picker-input');
  if (calBtn && datePicker) {
    calBtn.addEventListener('click', () => {
      if (datePicker.showPicker) {
        datePicker.showPicker();
      } else {
        datePicker.click();
      }
    });

    datePicker.addEventListener('change', (e) => {
      if (e.target.value) {
        const key = isoToKey(e.target.value);
        selectDate(key);
      }
    });
  }

  // Arama modali
  setupSearch();

  // Klavye kısayolları
  document.addEventListener('keydown', (e) => {
    if (e.target.closest('input, textarea, select, [contenteditable="true"]')) return;

    if (e.key === 'ArrowLeft') {
      e.preventDefault();
      go(-1);
    } else if (e.key === 'ArrowRight') {
      e.preventDefault();
      go(1);
    } else if (e.key === 't' || e.key === 'T') {
      selectDate(state.today);
    } else if (e.key === '/' || (e.ctrlKey && e.key.toLowerCase() === 'k')) {
      e.preventDefault();
      const modal = $('search-modal');
      if (modal && !modal.open) {
        $('btn-search')?.click();
      }
    }
  });

  // Dokunmatik: kartlar üzerinde yatay kaydırma (swipe)
  const grid = $('menu-grid');
  let sx = null, sy = 0, st = 0;
  grid.addEventListener('touchstart', (e) => {
    if (e.touches.length !== 1) { sx = null; return; }
    sx = e.touches[0].clientX;
    sy = e.touches[0].clientY;
    st = performance.now();
  }, { passive: true });

  grid.addEventListener('touchend', (e) => {
    if (sx === null) return;
    const t  = e.changedTouches[0];
    const dx = t.clientX - sx;
    const dy = t.clientY - sy;
    sx = null;
    if (performance.now() - st > 700) return;
    if (Math.abs(dx) > CONFIG.swipeThreshold && Math.abs(dx) > Math.abs(dy) * 1.5) {
      go(dx < 0 ? 1 : -1);
    }
  }, { passive: true });
}

/* ═══════════════════════════════════════════════════════════════
   SAAT — saniye sınırına hizalı; sekme gizliyken durur.
   ═══════════════════════════════════════════════════════════════ */
function tick() {
  const now = new Date();
  $('header-clock').textContent = timeFmt.format(now);

  const t = todayKey(now);
  if (t !== state.today && state.sources) {
    const wasFollowing = state.selected === state.today;
    state.today = t;
    if (window.QuoteManager && typeof QuoteManager.onDayChange === 'function') {
      QuoteManager.onDayChange(t);
    }
    recomputeBounds();
    buildStrip();
    if (wasFollowing) state.selected = t;
    render(false);
  }

  clearTimeout(clockTimer);
  clockTimer = setTimeout(tick, 1000 - (Date.now() % 1000) + 5);
}

document.addEventListener('visibilitychange', () => {
  if (document.hidden) clearTimeout(clockTimer);
  else tick();
});

/* ═══════════════════════════════════════════════════════════════
   MAIN
   ═══════════════════════════════════════════════════════════════ */
async function main() {
  state.today = state.selected = todayKey();
  $('header-clock').textContent = timeFmt.format(new Date());
  renderHeader();

  // Mobil başlangıçta saat 14:00'dan sonra ise akşam yemeğini öne çıkar
  const currentHour = new Date().getHours();
  if (window.innerWidth < 860) {
    setMealFilter(currentHour >= 14 ? 'evening' : 'morning');
  } else {
    setMealFilter('all');
  }

  const [m, e] = await Promise.allSettled([
    ExcelReader.createMenuSource(CONFIG.morningFile, 'morning'),
    ExcelReader.createMenuSource(CONFIG.eveningFile, 'evening'),
  ]);

  const errors = [];
  [['morning', m, 'Sabah kahvaltısı'], ['evening', e, 'Akşam yemeği']].forEach(([kind, r, label]) => {
    if (r.status === 'fulfilled') {
      state.sources[kind] = r.value;
    } else {
      console.error(`[MenuApp] ${label} hatası:`, r.reason);
      state.errors[kind] = r.reason?.message || 'Bilinmeyen hata';
      errors.push(`${label} yüklenemedi: ${state.errors[kind]}`);
    }
  });
  if (errors.length) showError(errors);

  const dateSet = new Set([
    ...(state.sources.morning?.dates || []),
    ...(state.sources.evening?.dates || []),
  ]);
  state.dates = [...dateSet].sort((a, b) => keyToUTC(a) - keyToUTC(b));

  recomputeBounds();

  // Bugün menü listesinde yoksa (ör. farklı ayda açıldıysa) menüsü olan en yakın güne ayarla
  if (!dateSet.has(state.today) && state.dates.length > 0) {
    state.selected = state.dates[0];
  }

  // Tarih seçici girdisinin sınırlarını ayarla
  const datePicker = $('date-picker-input');
  if (datePicker && state.dates.length > 0) {
    datePicker.min = keyToISO(state.dates[0]);
    datePicker.max = keyToISO(state.dates[state.dates.length - 1]);
    datePicker.value = keyToISO(state.selected);
  }

  buildStrip();
  renderNotes();
  if (window.QuoteManager) {
    QuoteManager.init(state.today);
  }
  bindEvents();
  render(false);

  $('footer-time').textContent = new Date().toLocaleString('tr-TR', {
    timeZone: CONFIG.timeZone,
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit',
  });

  // PWA Service Worker kaydı
  if ('serviceWorker' in navigator && location.protocol.startsWith('http')) {
    navigator.serviceWorker.register('sw.js').catch(() => {});
  }

  tick();
}

/* ── INIT ────────────────────────────────────────────────────── */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', main);
} else {
  main();
}
