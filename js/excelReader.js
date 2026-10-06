/**
 * excelReader.js  — v3.0
 * ──────────────────────────────────────────────────────────────
 * v3.0: JSON veri desteği (data/*.json + gömülü data/*.js),
 *       createMenuSource() ile tüm ayı tek seferde okuma,
 *       SheetJS yalnızca .xlsx gerektiğinde tembel yüklenir.
 *
 * Gerçek Excel yapısına göre yeniden yazıldı.
 *
 * SABAH (sabah_kahvaltisi.xlsx — sheet: KAHVALTI)
 *   • Her haftalık blok: tarih satırı (datetime) + altındaki yemek satırları
 *   • Tarih satırı: col 1 | col 4 | col 7 | col 10 | col 13 | col 16 | col 19
 *     (her 3 sütunda bir, "Gramaj" ve "Fiyat" atlanarak)
 *   • O günün yemek isimleri: tarih sütununun hemen altındaki satırlar boyunca,
 *     aynı sütun ofseti üzerinde yer alır.
 *   • "Gramaj" veya "Fiyat" içeren sütun değerleri gösterilmez.
 *   • Çeyrek Ekmek / Su / Çay sabit olduğu için ayrıca gösterilmez (isteğe bağlı).
 *
 * AKSAM (aksam_yemegi.xlsx — sheet: YEMEK)
 *   • Tarih satırı: col 2 | col 5 | col 8 | col 11 | col 14 | col 17 | col 20
 *     (col 1 = "YEMEK ÇEŞİTLERİ" etiketi)
 *   • Yemek isimleri: col 1'deki "1.Yemek Çeşitleri" vb. satırlarda, tarih sütunu
 *     ofseti üzerinde yer alır.
 *
 * Ortak tarama mantığı:
 *   1. Tüm sayfayı satır x sütun dizisine dök.
 *   2. Her satırı tara: datetime değeri içeren hücre = tarih bloğu başlangıcı.
 *   3. O tarihten sonraki satırları (sonraki tarih bloğuna kadar) yemek satırı say.
 *   4. Bugünün tarihine karşılık gelen sütun ofseti altındaki değerleri topla.
 */

const ExcelReader = (() => {

  /* ── Yardımcı: JS Date → "DD.MM.YYYY" ─────────────────────── */
  function dateToStr(d) {
    const day   = String(d.getDate()).padStart(2, '0');
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const year  = String(d.getFullYear());
    return `${day}.${month}.${year}`;
  }

  /* ── Yardımcı: Hücre değerinin JS Date mi olduğunu kontrol ── */
  function isDateValue(v) {
    return v instanceof Date && !isNaN(v.getTime());
  }

  /* ── Yardımcı: Gizlenecek sabit öğeler ──────────────────────
     Çeyrek Ekmek / Su / Çay her gün aynı olduğu için
     kartlarda tekrar göstermiyoruz.                           */
  const SKIP_PATTERNS = [
    /^çeyrek ekmek/i,
    /^500 ml/i,
    /^\*\*çay/i,
    /^\*\*çay\/bitki/i,
    /^gramaj$/i,
    /^fiyat$/i,
  ];

  function shouldSkip(text) {
    if (!text) return true;
    const t = String(text).trim();
    if (t === '') return true;
    return SKIP_PATTERNS.some(re => re.test(t));
  }

  /* ── Yardımcı: Gramaj string'ini yemek adından ayır ─────────
     Bazı hücrelerde "Yemek adı\ngramaj" şeklinde çift satır var. */
  function cleanFoodName(text) {
    if (!text) return '';
    return String(text).split('\n')[0].trim();
  }

  /**
   * SheetJS workbook'u raw 2D diziye çevirir (0-indexed).
   * cellDates: true ile Date objeleri döner.
   * @param {object} wb - XLSX workbook
   * @param {string} sheetName
   * @returns {Array<Array>} grid[row][col]
   */
  function workbookToGrid(wb, sheetName) {
    const ws = wb.Sheets[sheetName];
    if (!ws) throw new Error(`Sheet bulunamadı: ${sheetName}`);
    const raw = XLSX.utils.sheet_to_json(ws, {
      header: 1,
      defval: null,
      raw: false,          // Tarihleri string olarak al (cellDates ile birlikte)
    });

    // cellDates: true ile ayrıca parse ediyoruz
    // XLSX.utils.sheet_to_json raw:false ile ISO string döner → Date'e çevir
    return raw;
  }

  /**
   * ISO tarih stringini JS Date objesine çevirir (eğer geçerliyse).
   * XLSX raw:false modu tarihleri "M/D/YY" veya "DD/MM/YYYY" gibi döndürebilir.
   * Bu nedenle raw:true ile tekrar okuyup cellDates kullanacağız.
   */
  function workbookToGridWithDates(wb, sheetName) {
    const ws = wb.Sheets[sheetName];
    if (!ws) throw new Error(`Sheet bulunamadı: ${sheetName}`);
    // raw:true → sayısal değerler, Date'ler JS Date objesi
    const raw = XLSX.utils.sheet_to_json(ws, {
      header: 1,
      defval: null,
      raw: true,
    });
    return raw;
  }

  /**
   * Sayısal Excel tarih serisini JS Date'e çevirir.
   * SheetJS raw:true modunda tarihler bazen sayı olarak gelir.
   */
  function excelSerialToDate(serial) {
    // Excel epoch: 1 Ocak 1900 (Windows), seri 1 = 01.01.1900
    // JS epoch: 1 Ocak 1970
    const MS_PER_DAY = 86400000;
    // Excel'de 60. gün (29 Şubat 1900) hatalı, kompanzasyon:
    const excelEpoch = new Date(1899, 11, 30); // 30 Aralık 1899
    return new Date(excelEpoch.getTime() + serial * MS_PER_DAY);
  }

  /**
   * Bir değerin tarih olup olmadığını ve "DD.MM.YYYY" stringini döndürür.
   * @param {*} value - Ham hücre değeri (raw:true modunda)
   * @returns {string|null}
   */
  function extractDateStr(value) {
    if (value === null || value === undefined) return null;

    // openpyxl/SheetJS Date objesi
    if (value instanceof Date && !isNaN(value.getTime())) {
      return dateToStr(value);
    }

    // Sayısal serial (SheetJS raw:true'da)
    if (typeof value === 'number' && value > 40000 && value < 60000) {
      const d = excelSerialToDate(value);
      if (!isNaN(d.getTime())) return dateToStr(d);
    }

    // String tarih (çeşitli formatlar)
    if (typeof value === 'string') {
      const s = value.trim();
      // DD.MM.YYYY
      const m1 = s.match(/^(\d{1,2})\.(\d{1,2})\.(\d{4})$/);
      if (m1) return `${m1[1].padStart(2,'0')}.${m1[2].padStart(2,'0')}.${m1[3]}`;
      // M/D/YY veya MM/DD/YYYY
      const m2 = s.match(/^(\d{1,2})\/(\d{1,2})\/(\d{2,4})$/);
      if (m2) {
        const yr = m2[3].length === 2 ? '20' + m2[3] : m2[3];
        return `${m2[2].padStart(2,'0')}.${m2[1].padStart(2,'0')}.${yr}`;
      }
      // YYYY-MM-DD
      const m3 = s.match(/^(\d{4})-(\d{2})-(\d{2})/);
      if (m3) return `${m3[3]}.${m3[2]}.${m3[1]}`;
    }

    return null;
  }

  /**
   * ─────────────────────────────────────────────────────────────
   * SABAH KAHVALTI okuyucu
   *
   * Yapı:
   *   Tarih satırı: col 0, 3, 6, 9, 12, 15, 18  (0-indexed)
   *                 "Gramaj" col 1, 4, 7...
   *                 "Fiyat"  col 2, 5, 8...
   *   Yemek satırları: tarih satırının hemen altından
   *                    bir sonraki tarih satırına kadar
   * ─────────────────────────────────────────────────────────────
   */
  function parseSabah(grid, targetDateStr) {
    // Sabah'ta tarihler col 0, 3, 6, 9, 12, 15, 18 (0-indexed)
    const DATE_COLS_SABAH = [0, 3, 6, 9, 12, 15, 18];

    // Tarih bloğu başlangıç satırlarını bul
    // Bir satırda DATE_COLS_SABAH'tan herhangi birinde tarih varsa → başlık satırı
    const blocks = []; // { rowIdx, colOffsets: [{col, dateStr}] }

    for (let r = 0; r < grid.length; r++) {
      const row = grid[r];
      if (!row) continue;
      const dateCols = [];
      for (const col of DATE_COLS_SABAH) {
        const ds = extractDateStr(row[col]);
        if (ds) dateCols.push({ col, dateStr: ds });
      }
      if (dateCols.length > 0) {
        blocks.push({ rowIdx: r, dateCols });
      }
    }

    // Hedef tarihi içeren bloğu ve sütunu bul
    let targetCol = null;
    let blockStart = null;
    let blockEnd = null;

    for (let bi = 0; bi < blocks.length; bi++) {
      const block = blocks[bi];
      for (const { col, dateStr } of block.dateCols) {
        if (dateStr === targetDateStr) {
          targetCol  = col;
          blockStart = block.rowIdx + 1; // Tarih satırının bir altı
          blockEnd   = bi + 1 < blocks.length
            ? blocks[bi + 1].rowIdx - 1
            : grid.length - 1;
          break;
        }
      }
      if (targetCol !== null) break;
    }

    if (targetCol === null) return null; // Tarih bulunamadı

    // O sütundaki yemek isimlerini topla
    const foods = [];
    for (let r = blockStart; r <= blockEnd; r++) {
      const row = grid[r];
      if (!row) continue;
      const val = row[targetCol];
      if (val === null || val === undefined) continue;
      const text = cleanFoodName(String(val));
      if (!shouldSkip(text)) {
        foods.push(text);
      }
    }

    return { foods, calories: null };
  }

  /**
   * ─────────────────────────────────────────────────────────────
   * AKŞAM YEMEĞİ okuyucu
   *
   * Yapı:
   *   col 0 = "YEMEK ÇEŞİTLERİ" / "1.Yemek Çeşitleri" vb.
   *   Tarih satırı: col 1, 4, 7, 10, 13, 16, 19  (0-indexed)
   *   Yemek değerleri: o sütunun hemen altından bir sonraki
   *                    tarih satırına kadar aynı sütunda
   * ─────────────────────────────────────────────────────────────
   */
  function parseAksam(grid, targetDateStr) {
    const DATE_COLS_AKSAM = [1, 4, 7, 10, 13, 16, 19];

    const blocks = [];
    for (let r = 0; r < grid.length; r++) {
      const row = grid[r];
      if (!row) continue;
      const dateCols = [];
      for (const col of DATE_COLS_AKSAM) {
        const ds = extractDateStr(row[col]);
        if (ds) dateCols.push({ col, dateStr: ds });
      }
      if (dateCols.length > 0) {
        blocks.push({ rowIdx: r, dateCols });
      }
    }

    let targetCol = null;
    let blockStart = null;
    let blockEnd = null;

    for (let bi = 0; bi < blocks.length; bi++) {
      const block = blocks[bi];
      for (const { col, dateStr } of block.dateCols) {
        if (dateStr === targetDateStr) {
          targetCol  = col;
          blockStart = block.rowIdx + 1;
          blockEnd   = bi + 1 < blocks.length
            ? blocks[bi + 1].rowIdx - 1
            : grid.length - 1;
          break;
        }
      }
      if (targetCol !== null) break;
    }

    if (targetCol === null) return null;

    const foods = [];
    for (let r = blockStart; r <= blockEnd; r++) {
      const row = grid[r];
      if (!row) continue;
      const val = row[targetCol];
      if (val === null || val === undefined) continue;
      const text = cleanFoodName(String(val));
      if (!shouldSkip(text)) {
        // Eğer birden fazla seçenek "/" ile ayrılıyorsa tek item olarak göster
        foods.push(text);
      }
    }

    return { foods, calories: null };
  }

  /* ═══════════════════════════════════════════════════════════
     SheetJS — TEMBEL YÜKLEME
     Kütüphane (~900 KB) yalnızca bir .xlsx dosyası okunacağı zaman
     indirilir. JSON verisiyle çalışırken hiç yüklenmez.
     ═══════════════════════════════════════════════════════════ */
  const SHEETJS_URL = 'https://cdn.sheetjs.com/xlsx-0.20.1/package/dist/xlsx.full.min.js';
  let sheetJsPromise = null;

  function ensureSheetJS() {
    if (window.XLSX) return Promise.resolve();
    if (!sheetJsPromise) {
      sheetJsPromise = new Promise((resolve, reject) => {
        const s = document.createElement('script');
        s.src = SHEETJS_URL;
        s.async = true;
        s.onload = () => resolve();
        s.onerror = () => {
          sheetJsPromise = null;
          reject(new Error('SheetJS kütüphanesi yüklenemedi'));
        };
        document.head.appendChild(s);
      });
    }
    return sheetJsPromise;
  }

  /**
   * Dosyayı fetch + SheetJS ile yükler ve grid döndürür.
   * @param {string} filePath
   * @param {string} sheetName
   * @returns {Promise<Array[]>}
   */
  async function loadGrid(filePath, sheetName) {
    await ensureSheetJS();
    const response = await fetch(filePath, { cache: 'no-cache' });
    if (!response.ok) throw new Error(`HTTP ${response.status}: ${filePath}`);
    const buf = await response.arrayBuffer();
    const wb  = XLSX.read(buf, { type: 'array', cellDates: true, raw: true });
    // cellDates:true → Date objelerini JS Date olarak verir
    const ws  = wb.Sheets[sheetName];
    if (!ws) throw new Error(`"${sheetName}" sayfası bulunamadı`);
    const grid = XLSX.utils.sheet_to_json(ws, {
      header: 1,
      defval: null,
      raw: true,
    });
    return grid;
  }

  /** Excel grid'indeki tüm tarihleri toplar (gün şeridi için). */
  function collectDates(grid, cols) {
    const set = new Set();
    for (const row of grid) {
      if (!row) continue;
      for (const c of cols) {
        const ds = extractDateStr(row[c]);
        if (ds) set.add(ds);
      }
    }
    return [...set];
  }

  /* ═══════════════════════════════════════════════════════════
     JSON / GÖMÜLÜ VERİ
     ═══════════════════════════════════════════════════════════ */

  /** "6.10.2026" → "06.10.2026" */
  function normalizeDateKey(str) {
    const s = String(str || '').trim();
    const p = s.split('.');
    if (p.length !== 3) return s;
    return `${p[0].padStart(2, '0')}.${p[1].padStart(2, '0')}.${p[2]}`;
  }

  /* Her öğünde sabit verilen ekmek / su / çay */
  const EXTRA_PATTERNS = [/^\**\s*çeyrek ekmek/i, /^\**\s*500 ml/i, /^\**\s*çay/i];
  function isExtra(text) {
    const t = String(text || '').trim();
    return EXTRA_PATTERNS.some(re => re.test(t));
  }

  /** Karşılaştırma anahtarı: küçük harf, boşluksuz, tekil "/" */
  function compactName(s) {
    return String(s || '')
      .toLocaleLowerCase('tr')
      .replace(/\*/g, '')
      .replace(/\s+/g, '')
      .replace(/\/+/g, '/');
  }

  /**
   * Ham gün kaydını görünüm modeline çevirir.
   * yemekler[] (temiz isimler) ile ogeler[] (gramaj/kategori) eşleştirilir;
   * eşleşmeyen sabit öğeler "extras" olarak ayrılır.
   */
  function normalizeDay(day) {
    if (!day) return null;
    const names  = day.yemekler || day.foods || [];
    const ogeler = Array.isArray(day.ogeler) ? day.ogeler : [];
    const used   = new Set();

    const items = names.map((name, i) => {
      const key = compactName(name);
      let idx = ogeler.findIndex((o, j) => !used.has(j) && compactName(o.ad) === key);
      if (idx === -1 && ogeler[i] && !used.has(i) && !isExtra(ogeler[i].ad)) idx = i;
      if (idx !== -1) used.add(idx);
      const o = idx !== -1 ? ogeler[idx] : {};
      return {
        name:     String(name).trim(),
        gramaj:   o.gramaj   || '',
        enerji:   o.enerji   || '',
        kategori: o.kategori || '',
      };
    });

    const extras = ogeler
      .filter((o, j) => !used.has(j) && isExtra(o.ad))
      .map(o => String(o.ad).replace(/^\*+\s*/, '').trim());

    return {
      foods:    items.map(it => it.name),
      items,
      extras,
      calories: day.calories || day.kalori || null,
    };
  }

  const jsonCache = new Map();

  /**
   * JSON verisini yükler. data/*.js ile gömülü global varsa ağ isteği
   * yapılmaz (file:// ile açıldığında da çalışır, çift indirme olmaz).
   */
  function loadJsonData(filePath, globalName) {
    if (globalName && window[globalName]) return Promise.resolve(window[globalName]);
    if (!jsonCache.has(filePath)) {
      const p = fetch(filePath, { cache: 'no-cache' })
        .then(r => {
          if (!r.ok) throw new Error(`HTTP ${r.status}: ${filePath}`);
          return r.json();
        })
        .catch(err => {
          jsonCache.delete(filePath);
          if (err instanceof TypeError) {
            throw new Error(`${filePath} okunamadı (data/*.js dosyası eksik veya tarayıcı yerel dosya erişimini engelledi)`);
          }
          throw err;
        });
      jsonCache.set(filePath, p);
    }
    return jsonCache.get(filePath);
  }

  /**
   * Bir öğün için veri kaynağı oluşturur.
   * @param {string} filePath  .json veya .xlsx
   * @param {'morning'|'evening'} kind
   * @returns {Promise<{kind, title, notes, signature, dates: string[], getDay: (d:string)=>object|null}>}
   */
  async function createMenuSource(filePath, kind) {
    const isMorning = kind === 'morning';

    if (/\.json$/i.test(filePath)) {
      const data = await loadJsonData(filePath, isMorning ? 'MENU_DATA_SABAH' : 'MENU_DATA_AKSAM');
      const index = {};
      if (data.gunler) {
        for (const [k, v] of Object.entries(data.gunler)) index[normalizeDateKey(k)] = v;
      } else if (Array.isArray(data.liste)) {
        for (const v of data.liste) index[normalizeDateKey(v.tarih)] = v;
      }
      return {
        kind,
        title:     data.baslik || '',
        notes:     Array.isArray(data.notlar) ? data.notlar : [],
        signature: data.imza || null,
        dates:     Object.keys(index),
        getDay:    (dateStr) => normalizeDay(index[normalizeDateKey(dateStr)]),
      };
    }

    // Excel (eski format) — grid bir kez okunur, günler bellekten çözülür
    const grid  = await loadGrid(filePath, isMorning ? 'KAHVALTI' : 'YEMEK');
    const parse = isMorning ? parseSabah : parseAksam;
    const cols  = isMorning ? [0, 3, 6, 9, 12, 15, 18] : [1, 4, 7, 10, 13, 16, 19];
    return {
      kind,
      title:     '',
      notes:     [],
      signature: null,
      dates:     collectDates(grid, cols),
      getDay:    (dateStr) => {
        const r = parse(grid, normalizeDateKey(dateStr));
        return r ? normalizeDay({ yemekler: r.foods }) : null;
      },
    };
  }

  /** Geriye dönük uyumluluk: tek günlük sabah menüsü */
  async function getMorningMenu(filePath, targetDateStr) {
    return (await createMenuSource(filePath, 'morning')).getDay(targetDateStr);
  }

  /** Geriye dönük uyumluluk: tek günlük akşam menüsü */
  async function getEveningMenu(filePath, targetDateStr) {
    return (await createMenuSource(filePath, 'evening')).getDay(targetDateStr);
  }

  // Public API
  return { createMenuSource, getMorningMenu, getEveningMenu, normalizeDay };

})();
