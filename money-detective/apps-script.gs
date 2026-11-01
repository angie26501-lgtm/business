/**
 * 人生金錢偵探社｜財富航海群島：登島問卷 ＋ 自動產生通行碼
 * 部署方式：Apps Script →「部署」→「新增部署作業」→ 類型「網頁應用程式」
 *   執行身分：我　｜　存取權：任何人
 * 第一次執行會自動建立 Google 試算表「財富航海群島_登島問卷」，網址記在指令碼屬性 SHEET_ID。
 */
const SHEET_NAME = '登島問卷';
const HEAD = ['時間', '暱稱', 'LINE 名稱', 'Q1 最想解決', 'Q2 亞健康症狀', 'Q3 想說的話', '通行碼', '來源網址', '最後登入'];

function sheet_() {
  const props = PropertiesService.getScriptProperties();
  let id = props.getProperty('SHEET_ID'), ss;
  if (id) { try { ss = SpreadsheetApp.openById(id); } catch (e) { ss = null; } }
  if (!ss) {
    ss = SpreadsheetApp.create('財富航海群島_登島問卷');
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
    const rows = sh.getLastRow() > 1 ? sh.getRange(2, 1, sh.getLastRow() - 1, HEAD.length).getValues() : [];

    if (p.action === 'island_signup') {
      const nick = clean_(p.nick, 20), line = clean_(p.line, 30);
      if (!nick || !line || !p.q1 || !p.q2) return out_({ ok: false, err: 'missing' }, cb);
      // 同一個暱稱＋LINE 名稱再填一次 → 回傳原本的通行碼
      for (let i = 0; i < rows.length; i++) {
        if (rows[i][1] === nick && rows[i][2] === line) {
          sh.getRange(i + 2, 9).setValue(new Date());
          return out_({ ok: true, again: true, code: String(rows[i][6]), nick: nick }, cb);
        }
      }
      const used = new Set(rows.map(r => String(r[6])));
      let code;
      do { code = String(Math.floor(100000 + Math.random() * 900000)); } while (used.has(code));
      sh.appendRow([new Date(), nick, line, clean_(p.q1, 60), clean_(p.q2, 200), clean_(p.msg, 100), code, clean_(p.src, 200), new Date()]);
      sh.getRange(sh.getLastRow(), 7).setNumberFormat('@').setValue(code);
      return out_({ ok: true, again: false, code: code, nick: nick }, cb);
    }

    if (p.action === 'island_login') {
      const code = String(p.code || '').trim();
      for (let i = 0; i < rows.length; i++) {
        if (String(rows[i][6]) === code) {
          sh.getRange(i + 2, 9).setValue(new Date());
          return out_({ ok: true, nick: rows[i][1] }, cb);
        }
      }
      return out_({ ok: false, err: 'notfound' }, cb);
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
}
