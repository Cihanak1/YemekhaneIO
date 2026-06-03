/**
 * app.js  — v3.0
 * ──────────────────────────────────────────────────────────────
 * Günlük Menü Panosu — Ana Uygulama Mantığı
 *
 * YENİ: Staggered giriş animasyonları, clock-flip efekti,
 *       yemek item stagger, footer reveal.
 *
 * NOT: excelReader.js'e hiçbir değişiklik yapılmadı.
 */

'use strict';

/* ── CONFIG ─────────────────────────────────────────────────── */
const CONFIG = {
  morningFile:  'data/sabah_kahvaltisi.xlsx',
  eveningFile:  'data/aksam_yemegi.xlsx',

  morningIcons: ['🥚', '🧆', '🧀', '🫒', '🍞', '🍅', '🥛', '🍯', '🥜', '🫙'],
  eveningIcons: ['🍲', '🍖', '🥗', '🍚', '🥙', '🥕', '🫕', '🥘', '🍜', '🥗'],

  // Kademeli giriş gecikmeler (ms)
  stagger: {
    badge:    0,
    date:     200,
    day:      300,
    clock:    400,
    divider:  500,
    cardMorn: 650,
    cardEve:  780,
    itemBase: 900,   // İlk yemek öğesinin gecikmesi
    itemStep: 80,    // Her bir öğe arası
  },
};

/* ── STATE ───────────────────────────────────────────────────── */
let clockInterval  = null;
let prevClockStr   = '';   // Saat flip için önceki değer

/* ── UTILITY ─────────────────────────────────────────────────── */
function pad2(n) { return String(n).padStart(2, '0'); }

function getTodayTR() {
  const now = new Date();
  const day   = pad2(parseInt(now.toLocaleDateString('tr-TR', { timeZone: 'Europe/Istanbul', day: '2-digit' }), 10));
  const month = pad2(parseInt(now.toLocaleDateString('tr-TR', { timeZone: 'Europe/Istanbul', month: '2-digit' }), 10));
  const year  = now.toLocaleDateString('tr-TR', { timeZone: 'Europe/Istanbul', year: 'numeric' });
  const dateStr = `${day}.${month}.${year}`;

  const dayName = (() => {
    const s = now.toLocaleDateString('tr-TR', { timeZone: 'Europe/Istanbul', weekday: 'long' });
    return s.charAt(0).toUpperCase() + s.slice(1);
  })();

  const fullDate = now.toLocaleDateString('tr-TR', {
    timeZone: 'Europe/Istanbul',
    day: 'numeric', month: 'long', year: 'numeric'
  });

  return { dateStr, dayName, fullDate };
}

function getCurrentTimeTR() {
  return new Date().toLocaleTimeString('tr-TR', {
    timeZone: 'Europe/Istanbul',
    hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false
  });
}

/* ── DOM HELPERS ─────────────────────────────────────────────── */
function $(id) { return document.getElementById(id); }

function after(ms, fn) { return setTimeout(fn, ms); }

/**
 * Bir elementi belirlenen ms sonra görünür kılar (is-visible sınıfı).
 * @param {HTMLElement|string} elOrId
 * @param {number} delay - milisaniye
 */
function revealAfter(elOrId, delay) {
  const el = typeof elOrId === 'string' ? $(elOrId) : elOrId;
  if (!el) return;
  after(delay, () => el.classList.add('is-visible'));
}

/* ── LOADING ─────────────────────────────────────────────────── */
function hideLoading() {
  const overlay = $('loading-overlay');
  if (!overlay) return;
  overlay.classList.add('hidden');
  setTimeout(() => overlay.remove(), 600);
}

/* ── ERROR ───────────────────────────────────────────────────── */
function showError(message) {
  const container = $('error-container');
  if (!container) return;
  container.innerHTML = `
    <div class="error-banner" role="alert">
      <span class="error-banner-icon">⚠️</span>
      <span class="error-banner-text">${message}</span>
    </div>
  `;
}

/* ── XSS ─────────────────────────────────────────────────────── */
function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/* ═══════════════════════════════════════════════════════════════
   SAAT FLIP ANİMASYONU
   ─────────────────────────────────────────────────────────────
   Saniye değiştiğinde:
     1. Mevcut metin yukarı doğru uçar (clock-exit)
     2. Yeni metin alttan gelir (clock-enter → clock-enter-active)
   ═══════════════════════════════════════════════════════════════ */
function flipClock(el, newValue) {
  if (!el || el.textContent.trim() === newValue) return;

  // 1. Eski değeri yukarı uçur
  el.classList.add('clock-exit');

  // 2. Transition bittikten sonra yeni değeri alttan getir
  const FLIP_DUR = 180; // ms — CSS transition süresiyle eşleşmeli

  after(FLIP_DUR, () => {
    el.textContent = newValue;
    el.classList.remove('clock-exit');
    el.classList.add('clock-enter');

    // Tarayıcının reflow yapmasını zorla
    void el.offsetHeight;

    el.classList.add('clock-enter-active');
    el.classList.remove('clock-enter');

    after(FLIP_DUR, () => {
      el.classList.remove('clock-enter-active');
    });
  });
}

/* ═══════════════════════════════════════════════════════════════
   HEADER ANİMASYON SEKANSINI BAŞLAT
   ─────────────────────────────────────────────────────────────
   Staggered giriş: rozet → tarih → gün → saat → divider
   ═══════════════════════════════════════════════════════════════ */
function startHeaderEntrance() {
  const { stagger } = CONFIG;
  revealAfter('header-badge',    stagger.badge);
  revealAfter('header-date',     stagger.date);
  revealAfter('header-day',      stagger.day);
  revealAfter('header-clock',    stagger.clock);
  revealAfter('header-divider',  stagger.divider);
}

/* ── HEADER RENDER ───────────────────────────────────────────── */
function renderHeader() {
  const { dateStr, dayName, fullDate } = getTodayTR();

  const elDate  = $('header-date');
  const elDay   = $('header-day');
  const elClock = $('header-clock');

  if (elDate)  elDate.textContent  = fullDate;
  if (elDay)   elDay.textContent   = dayName;
  if (elClock) {
    elClock.textContent = getCurrentTimeTR();
    prevClockStr = elClock.textContent;
  }

  // Staggered entrance başlat
  startHeaderEntrance();

  // Saat — her saniye flip ile güncelle
  clearInterval(clockInterval);
  clockInterval = setInterval(() => {
    const newTime = getCurrentTimeTR();
    if (newTime !== prevClockStr) {
      flipClock(elClock, newTime);
      prevClockStr = newTime;
    }
  }, 1000);

  return dateStr;
}

/* ═══════════════════════════════════════════════════════════════
   YEMEK ITEMS — STAGGER ANİMASYONU
   ─────────────────────────────────────────────────────────────
   Her .food-item elemanı sırasıyla yukarı doğru belirir.
   ═══════════════════════════════════════════════════════════════ */

/**
 * Bir kart gövdesindeki tüm .food-item'ları stagger ile gösterir.
 * @param {HTMLElement} bodyEl  - Kart gövdesi
 * @param {number} baseDelay   - İlk öğenin ms gecikmesi
 * @param {number} step        - Öğeler arası ms
 */
function animateFoodItems(bodyEl, baseDelay, step) {
  if (!bodyEl) return;
  const items = bodyEl.querySelectorAll('.food-item');
  items.forEach((item, i) => {
    after(baseDelay + i * step, () => item.classList.add('is-visible'));
  });
}

/* ── YEMEK GRİD HTML ─────────────────────────────────────────── */
function buildFoodGrid(foods, icons) {
  if (!foods || foods.length === 0) {
    return `<p style="color:var(--text-muted);font-size:0.875rem;padding:8px 0;">Yemek bilgisi yüklenemedi.</p>`;
  }

  return `<div class="food-grid">${
    foods.map((food, i) => {
      const parts    = food.split('/').map(s => s.trim()).filter(Boolean);
      const mainName = escapeHtml(parts[0]);
      const altNames = parts.slice(1).map(escapeHtml).join(' / ');
      const icon     = icons[i % icons.length];

      return `
        <div class="food-item" title="${escapeHtml(food)}">
          <span class="food-item-index">${i + 1}</span>
          <span class="food-item-icon">${icon}</span>
          <span class="food-item-content">
            <span class="food-item-name">${mainName}</span>
            ${altNames ? `<span class="food-item-alt">/ ${altNames}</span>` : ''}
          </span>
        </div>
      `;
    }).join('')
  }</div>`;
}

/* ── KART RENDER ─────────────────────────────────────────────── */
function renderMenuCard(type, menu, cardDelay) {
  const isMorning = type === 'morning';
  const cardEl    = $(isMorning ? 'card-morning'      : 'card-evening');
  const noMenuEl  = $(isMorning ? 'no-menu-morning'   : 'no-menu-evening');
  const bodyEl    = $(isMorning ? 'card-morning-body' : 'card-evening-body');
  const calEl     = $(isMorning ? 'morning-calorie'   : 'evening-calorie');

  if (!menu || menu.foods.length === 0) {
    if (cardEl)   cardEl.style.display   = 'none';
    if (noMenuEl) noMenuEl.style.display = '';
    return;
  }

  if (cardEl)   cardEl.style.display   = '';
  if (noMenuEl) noMenuEl.style.display = 'none';

  // Kalori rozeti
  if (calEl) {
    calEl.innerHTML = menu.calories
      ? `<span class="card-calorie-badge">🔥 <strong>${menu.calories.toLocaleString('tr-TR')}</strong> kcal</span>`
      : '';
  }

  // Yemek grid'ini DOM'a yaz
  if (bodyEl) {
    const icons = isMorning ? CONFIG.morningIcons : CONFIG.eveningIcons;
    bodyEl.innerHTML = buildFoodGrid(menu.foods, icons);
  }

  // Kartı göster (stagger)
  revealAfter(cardEl, cardDelay);

  // Yemek öğelerini stagger ile canlandır
  const itemBase = cardDelay + 150;
  animateFoodItems(bodyEl, itemBase, CONFIG.stagger.itemStep);
}

/* ── HER İKİSİ DE BOŞ ───────────────────────────────────────── */
function renderBothEmpty() {
  const grid = $('menu-grid');
  if (!grid) return;
  grid.innerHTML = `
    <div class="empty-card" style="grid-column:1/-1">
      <div class="empty-card-icon">🍽️</div>
      <div class="empty-card-title">Bugün için menü girilmemiştir</div>
      <div class="empty-card-desc">
        Hafta sonu veya tatil nedeniyle bu günün menüsü bulunmamaktadır.<br>
        İyi dinlenceler! 🌿
      </div>
    </div>
  `;
}

/* ── FOOTER ──────────────────────────────────────────────────── */
function renderFooter() {
  const el = $('footer-time');
  if (el) {
    el.textContent = new Date().toLocaleString('tr-TR', {
      timeZone: 'Europe/Istanbul',
      day: '2-digit', month: '2-digit', year: 'numeric',
      hour: '2-digit', minute: '2-digit'
    });
  }
  // Footer'ı da kademeli göster
  after(1500, () => {
    const footer = $('app-footer');
    if (footer) footer.classList.add('is-visible');
  });
}

/* ═══════════════════════════════════════════════════════════════
   MAIN
   ═══════════════════════════════════════════════════════════════ */
async function main() {
  try {
    // 1. Header içeriğini doldur + stagger başlat
    const dateStr = renderHeader();

    // 2. İki Excel dosyasını paralel yükle
    const [morningResult, eveningResult] = await Promise.allSettled([
      ExcelReader.getMorningMenu(CONFIG.morningFile, dateStr),
      ExcelReader.getEveningMenu(CONFIG.eveningFile, dateStr),
    ]);

    const errors = [];

    let morningMenu = null;
    if (morningResult.status === 'fulfilled') {
      morningMenu = morningResult.value;
    } else {
      console.error('[MenuApp] Sabah hatası:', morningResult.reason);
      errors.push(`Sabah kahvaltısı yüklenemedi: ${morningResult.reason?.message || 'Hata'}`);
    }

    let eveningMenu = null;
    if (eveningResult.status === 'fulfilled') {
      eveningMenu = eveningResult.value;
    } else {
      console.error('[MenuApp] Akşam hatası:', eveningResult.reason);
      errors.push(`Akşam yemeği yüklenemedi: ${eveningResult.reason?.message || 'Hata'}`);
    }

    if (errors.length > 0) showError(errors.join('<br>'));

    // 3. UI'yi doldur
    if (!morningMenu && !eveningMenu && errors.length === 0) {
      renderBothEmpty();
    } else {
      // Sabah: soldan gelir (CSS'te tanımlı)
      renderMenuCard('morning', morningMenu, CONFIG.stagger.cardMorn);
      // Akşam: sağdan gelir (CSS'te tanımlı)
      renderMenuCard('evening', eveningMenu, CONFIG.stagger.cardEve);
    }

    renderFooter();

  } catch (err) {
    console.error('[MenuApp] Kritik hata:', err);
    showError(`Beklenmeyen hata: ${err.message}`);
  } finally {
    hideLoading();
  }
}

/* ── INIT ────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', main);
