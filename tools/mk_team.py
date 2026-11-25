# 由 yl-blackfriday.html 產生團隊主購版 yl-bf-team.html（不連芳療群組、不連芸琪私訊、不顯示預購名單）
import re, sys
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(ROOT, 'yl-blackfriday.html')
dst = os.path.join(ROOT, 'yl-bf-team.html')
h = open(src, encoding='utf-8').read()

def rep(a, b, n=None):
    global h
    c = h.count(a)
    if c == 0 or (n is not None and c != n):
        sys.exit(f'找不到或數量不符({c}): {a[:70]}')
    h = h.replace(a, b)

def cut(start, end, new=''):
    """把從 start 開始到 end（含）的一段換成 new"""
    global h
    i = h.find(start)
    if i < 0: sys.exit('cut 找不到: ' + start[:60])
    j = h.find(end, i)
    if j < 0: sys.exit('cut 找不到結尾: ' + end[:60])
    h = h[:i] + new + h[j + len(end):]

# ── 頁首 ──
rep('<link rel="manifest" href="yl-bf-manifest.json">', '')
rep('<meta name="apple-mobile-web-app-title" content="黑五美單">', '<meta name="apple-mobile-web-app-title" content="黑五主購">')
rep('<title>芳療好生活 芸琪共學圈｜黑五美單代購</title>', '<title>芳療好生活 芸琪共學圈｜馥芸團隊專屬｜黑五美單</title>')
rep('🌹 芳療好生活 芸琪共學圈｜芸琪 Angie', '🌹 芳療好生活 芸琪共學圈｜馥芸團隊專屬')
cut('<div class="me">', '</div>', '<div class="me"><button class="mw" id="a2h" type="button">📲 加到手機桌面</button></div>')
rep('群組接龍截止 <b>11/28（六）中午 12:00</b>', '美國官方黑五截止 <b>11/28 晚上（美國山區時間）</b><br><small style="color:var(--mut)">約台灣 11/29（日）下午 3 點</small>')
rep("new Date('2026-11-28T12:00:00+08:00')", "new Date('2026-11-29T14:59:00+08:00')")
rep('本次接龍已截止，感謝大家！', '美國官方黑五活動已結束')
rep('最終仍以官方金額及代購金額計算，芸琪會再統計後與您私訊核對確認。如有誤植，敬請見諒。', '最終以美國官網結帳金額為準。如有誤植，敬請見諒。')

# ── 不顯示預購名單 ──
rep("fetch('yl-bf-orders.json?t='+Date.now())", "Promise.resolve({ok:false})")

# ── 存檔 key 分開，不和主頁的購物車混在一起 ──
h = h.replace("'bf26cart'", "'bf26tcart'").replace("'bf26nm'", "'bf26tnm'").replace("'bf26tut'", "'bf26ttut'")

# ── 推薦、熱門文字 ──
h = h.replace('芸琪推薦', '推薦')
rep('📸 群組熱門', '📸 熱門品項')
rep('📸 芳療群組相本「熱門美單商品」裡的品項，依相本順序排列', '📸 團隊熱門美單品項')
rep('芸琪自己每天都在吃的日常營養補充。', '日常營養補充的熱門選擇。')
rep('以官網及芸琪確認為準', '以官網為準')
h = h.replace("'請問芸琪'", "'請洽主購'")
rep('，或私訊芸琪詢問', '')

# ── 購物清單用語 ──
rep('＋ 加入我的接龍', '＋ 加入購物清單')
rep('🛒 我的購物車', '🛒 購物清單')
rep('步驟 2｜填上你的名字', '步驟 2｜填上客戶或你的名字')
rep('placeholder="你的名字"', 'placeholder="客戶名字或你的名字"')
rep('步驟 3｜確認要貼到群組的文字', '步驟 3｜確認購物清單文字')
rep('📋 複製文字（下一步選群組或私訊）', '📋 複製購物清單')
rep('最後以實際統計後私訊核對金額為主</div>', '最後以美國官網結帳金額為準</div>')
h = h.replace('＊參考價，以私訊核對金額為主', '＊代購參考價，以官網結帳為準')
h = h.replace('以私訊核對金額為主', '以官網結帳為準')
h = h.replace('最後以實際統計後私訊核對金額為主', '最後以美國官網結帳金額為準')

# ── 第 5 步：只複製，不連群組／私訊 ──
cut('<div class="w2t">', '<button class="btn fin" id="fin">✅ 我貼好了，完成！</button>',
    '<div class="w2t">👇 第5步：把購物清單傳給你的主購人</div>'
    '<div class="wc wg"><ol><li><b>傳給你的主購人</b>：打開和主購人的私訊或群組</li><li>長按輸入框 →「貼上」→ 送出</li></ol><small>你是主購人？也可以貼到自己的群組、客戶私訊或記事本</small><br>'
    '<small>可以按「清空」再幫下一位客戶選，每位客戶各複製一份</small></div>'
    '<button class="btn fin" id="fin">✅ 我貼好了，完成！</button>')
rep('<b>完成囉！謝謝妳的支持 💕</b><p>芸琪統計後會私訊和妳核對最終金額 🙏<br>', '<b>完成囉！💕</b><p>主購人會再跟你核對金額與庫存 🙏<br>')
rep("t='✅ 第5步：選「貼到芳療群組」或「私訊貼給芸琪」→ 長按貼上送出 → 按「我貼好了」'", "t='✅ 第5步：把購物清單傳給你的主購人（私訊或群組）→ 貼上送出 → 按「我貼好了」'")
rep("t='🎉 全部完成！芸琪會私訊和妳核對金額，謝謝妳 💕'", "t='🎉 完成！要幫下一位客戶選，按「清空」重新開始'")
h = h.replace('「複製，去群組＋1」', '「📋 複製購物清單」')
rep('<i>5</i>貼上送出</div>', '<i>5</i>貼上使用</div>')

# ── 教學 ──
h = h.replace('寫群組裡大家認得的名字', '寫客戶名字或你的名字')
cut('<b>選一種方式貼上送出</b>', '就完成囉 🎉', '<b>傳給你的主購人</b><br>打開和主購人的私訊或群組，長按「貼上」送出；貼好後按金色「✅ 我貼好了」就完成囉 🎉')
h = h.replace('看預購名單', '查看購物清單')
h = h.replace('跟團超簡單', '整理清單超簡單')

# ── 說明分頁 ──
cut('<div class="box"><h3>📝 接龍格式</h3>', '</div>',
    '<div class="box"><h3>📝 怎麼用</h3>按「＋」選好品項，最下面按「選好了，下一步」，填上名字後按「複製購物清單」，就能傳給你的主購人（或貼到你的群組、客戶私訊）。<br><span style="color:var(--mut)">清單會列出產品編號、數量、美金、代購參考價和 PV，方便你到美國官網下單。</span></div>')
rep('本頁價格僅供參考，最終以官方金額及代購金額計算，芸琪統計後會私訊與您核對確認', '本頁價格僅供參考，最終以美國官網結帳金額為準')
rep('<li>黑五品項的產品編號，下單時芸琪幫大家對</li>', '<li>下單時請以產品編號核對品項</li>')
rep('<div class="box">有問題隨時問芸琪喔 💕</div>', '')
rep('<button data-t="how">📝 跟團</button>', '<button data-t="how">📝 說明</button>')
rep('⚠️ 價格僅供參考，最終以官方及代購金額計算，芸琪會再私訊核對確認。', '⚠️ 價格僅供參考，最終以美國官網結帳金額為準。')

# ── 複製文字加上美金，方便到官網下單 ──
rep("pv:bpv(r,i),pe:false}", "pv:bpv(r,i),pe:false,usd:r.mem}")
rep("all['r'+i]={k:'r'+i,code:r.code,n:r.n,nt:r.nt,pv:r.pv||0}", "all['r'+i]={k:'r'+i,code:r.code,n:r.n,nt:r.nt,pv:r.pv||0,usd:r.usd||0}")
rep("all['u'+i]={k:'u'+i,code:r.code,n:r.n,nt:r.nt,pv:r.pv||0}", "all['u'+i]={k:'u'+i,code:r.code,n:r.n,nt:r.nt,pv:r.pv||0,usd:r.usd||0}")
rep("all['n'+i]={k:'n'+i,code:r.code,n:r.n,nt:r.nt,pv:r.pv||0}", "all['n'+i]={k:'n'+i,code:r.code,n:r.n,nt:r.nt,pv:r.pv||0,usd:r.usd||0}")
rep("X${cart[k]}　$${fmt(all[k].nt*cart[k])}　${pvf((all[k].pv||0)*cart[k])}PV`", "X${cart[k]}　US$${((all[k].usd||0)*cart[k]).toFixed(2)}　NT$${fmt(all[k].nt*cart[k])}　${pvf((all[k].pv||0)*cart[k])}PV`")
rep("`合計 ${ks.length} 項：$${fmt(tot)}・${pvf(pvs(ks))}PV`", "`合計 ${ks.length} 項：US$${ks.reduce((s,k)=>s+(all[k].usd||0)*cart[k],0).toFixed(2)}・NT$${fmt(tot)}・${pvf(pvs(ks))}PV`")
open(dst, 'w', encoding='utf-8').write(h)

left = [m for m in re.findall(r'[^<>"\'`\n]{0,20}(?:芸琪|芳療群組|line\.me|接龍)[^<>"\'`\n]{0,20}', re.sub(r'const D=\{.*?\};\n', '', h, flags=re.S))]
print('剩下的字：', left)
