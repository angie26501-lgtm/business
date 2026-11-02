/**
 * 人生金錢偵探社｜三日營＋五日營任務進度（給管理者頁面 admin.html 看成員學習進度）
 * 部署方式：
 *   1. 到 https://script.google.com 新增專案，把這整份貼上（取代原本內容）
 *   2. 把下面 ADMIN_KEY 改成你的管理密碼（公開 GitHub 上這份是空白的，請勿把密碼推上 GitHub）
 *   3. 上方選 setup → 按「執行」→ 完成授權（會自動建立試算表「財富航海群島_營隊任務進度」）
 *   4.「部署」→「新增部署作業」→ 類型「網頁應用程式」｜執行身分：我｜存取權：任何人 → 複製網址（…/exec）
 *   5. 把網址填進 index.html 與 admin.html 的 PROGRESS_URL
 */
const ADMIN_KEY = '';
const SHEET_NAME = '五日營任務進度';
const HEAD = ['識別碼', '夥伴編號', '暱稱', '手機末3碼', '五日 Day 1', '五日 Day 2', '五日 Day 3', '五日 Day 4', '五日 Day 5', '五日加碼（11月第一筆記帳）', '五日營完成天數', '三日 DAY 1', '三日 DAY 2', '三日 DAY 3', '三日加碼（DAY4 學習包）', '三日營完成天數', '第一次登記', '最後更新'];

function sheet_() {
  const props = PropertiesService.getScriptProperties();
  let id = props.getProperty('SHEET_ID'), ss;
  if (id) { try { ss = SpreadsheetApp.openById(id); } catch (e) { ss = null; } }
  if (!ss) {
    ss = SpreadsheetApp.create('財富航海群島_營隊任務進度');
    props.setProperty('SHEET_ID', ss.getId());
    const sh = ss.getSheets()[0];
    sh.setName(SHEET_NAME);
    sh.appendRow(HEAD);
    sh.setFrozenRows(1);
  }
  return ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
}

function out_(obj, cb) {
  const s = JSON.stringify(obj);
  if (cb && /^[A-Za-z0-9_]+$/.test(cb)) {
    return ContentService.createTextOutput(cb + '(' + s + ')').setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService.createTextOutput(s).setMimeType(ContentService.MimeType.JSON);
}

function clean_(v, n) { return String(v || '').replace(/^[=+\-@]/, "'").trim().slice(0, n); }

function doGet(e) {
  const p = (e && e.parameter) || {}, cb = p.callback;
  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(10000);
    const sh = sheet_();
    const n = sh.getLastRow() > 1 ? sh.getLastRow() - 1 : 0;
    const rows = n ? sh.getRange(2, 1, n, HEAD.length).getValues() : [];

    if (p.action === 'camp_save') {
      const uid = clean_(p.uid, 60), nick = clean_(p.nick, 20);
      const prog = String(p.p || '000000'), prog3 = String(p.p3 || '0000');
      if (!uid || !nick || !/^[0-3]{5}[01]$/.test(prog) || !/^[0-3]{3}[01]$/.test(prog3)) return out_({ ok: false, err: 'missing' }, cb);
      const d = prog.slice(0, 5).split('').map(Number), bonus = Number(prog[5]);
      const d3 = prog3.slice(0, 3).split('').map(Number), bonus3 = Number(prog3[3]);
      const vals = [uid, clean_(p.qid, 20), nick, clean_(p.tail, 3), d[0], d[1], d[2], d[3], d[4], bonus, d.filter(x => x === 3).length,
        d3[0], d3[1], d3[2], bonus3, d3.filter(x => x === 3).length];
      for (let i = 0; i < rows.length; i++) {
        if (String(rows[i][0]) === uid) {
          sh.getRange(i + 2, 1, 1, vals.length).setValues([vals]);
          sh.getRange(i + 2, 18).setValue(new Date());
          return out_({ ok: true, again: true }, cb);
        }
      }
      sh.appendRow(vals.concat([new Date(), new Date()]));
      sh.getRange(sh.getLastRow(), 2, 1, 3).setNumberFormat('@').setValues([[vals[1], vals[2], vals[3]]]);
      return out_({ ok: true, again: false }, cb);
    }

    if (p.action === 'admin_progress') {
      if (!ADMIN_KEY || String(p.key || '') !== ADMIN_KEY) return out_({ ok: false, err: 'key' }, cb);
      const fmt = v => v instanceof Date ? Utilities.formatDate(v, 'Asia/Taipei', 'MM/dd HH:mm') : String(v || '');
      return out_({ ok: true, sheet: sh.getParent().getUrl(), rows: rows.map(r => ({
        uid: String(r[0]), qid: String(r[1]), nick: String(r[2]), tail: String(r[3]),
        d: [r[4], r[5], r[6], r[7], r[8]].map(x => Number(x) || 0), bonus: Number(r[9]) || 0, days: Number(r[10]) || 0,
        d3: [r[11], r[12], r[13]].map(x => Number(x) || 0), bonus3: Number(r[14]) || 0, days3: Number(r[15]) || 0,
        first: fmt(r[16]), last: fmt(r[17])
      })) }, cb);
    }

    return out_({ ok: false, err: 'unknown action' }, cb);
  } catch (err) {
    return out_({ ok: false, err: String(err) }, cb);
  } finally {
    try { lock.releaseLock(); } catch (e) {}
  }
}

/** 在編輯器按「執行」這個函式一次，可完成授權並建立試算表；執行紀錄會印出試算表網址 */
function setup() {
  const sh = sheet_();
  Logger.log(sh.getParent().getUrl());
  if (!ADMIN_KEY) Logger.log('⚠️ 請先把最上面的 ADMIN_KEY 改成你的管理密碼');
}
