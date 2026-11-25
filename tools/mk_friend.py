# 由 yl-blackfriday.html 產生好友版 yl-bf-friend.html（給艾多美等其他群組的朋友：只私訊芸琪，不連芳療群組、不顯示預購名單）
import re, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
h = open(os.path.join(ROOT, 'yl-blackfriday.html'), encoding='utf-8').read()

def rep(a, b):
    global h
    if a not in h: sys.exit('找不到: ' + a[:70])
    h = h.replace(a, b)

def cut(start, end, new=''):
    global h
    i = h.find(start)
    if i < 0: sys.exit('cut 找不到: ' + start[:60])
    j = h.find(end, i)
    if j < 0: sys.exit('cut 找不到結尾: ' + end[:60])
    h = h[:i] + new + h[j + len(end):]

rep('<link rel="manifest" href="yl-bf-manifest.json">', '')
rep('<title>芳療好生活 芸琪共學圈｜黑五美單代購</title>', '<title>芸琪 Angie｜YL 黑五美單代購（好友版）</title>')
rep('🌹 芳療好生活 芸琪共學圈｜芸琪 Angie', '🌹 芸琪 Angie｜YL 美單代購・好友專屬')
rep("fetch('yl-bf-orders.json?t='+Date.now())", "Promise.resolve({ok:false})")
h = h.replace("'bf26cart'", "'bf26fcart'").replace("'bf26nm'", "'bf26fnm'").replace("'bf26tut'", "'bf26ftut'")
rep('📸 芳療群組相本「熱門美單商品」裡的品項，依相本順序排列', '📸 熱門美單品項')
rep('📸 群組熱門', '📸 熱門品項')

# 第 5 步：只私訊芸琪
cut('<div class="w2t">', '<button class="btn fin" id="fin">',
    '<div class="w2t">👇 第5步：私訊貼給芸琪</div>'
    '<div class="w2"><div class="wc wb"><b>私訊貼給芸琪</b><a class="gome" href="https://line.me/ti/p/KbrYxqk7Rq" target="_blank" rel="noopener">✉️ 打開芸琪私訊 ➜</a>'
    '<ol><li>進到和芸琪的聊天室</li><li>長按輸入框 →「貼上」→ 送出</li></ol><small>還沒加芸琪好友？按上面按鈕就能加</small></div></div>'
    '<button class="btn fin" id="fin">')
rep('📋 複製文字（下一步選群組或私訊）', '📋 複製文字（下一步私訊芸琪）')
rep("t='✅ 第5步：選「貼到芳療群組」或「私訊貼給芸琪」→ 長按貼上送出 → 按「我貼好了」'", "t='✅ 第5步：打開芸琪私訊 → 長按貼上送出 → 按「我貼好了」'")
h = h.replace('「複製，去群組＋1」', '「📋 複製文字」')
cut('<b>選一種方式貼上送出</b>', '就完成囉 🎉', '<b>私訊貼給芸琪</b><br>打開芸琪私訊 → 長按「貼上」→ 送出；貼好後按金色「✅ 我貼好了」就完成囉 🎉')
h = h.replace('寫群組裡大家認得的名字', '寫芸琪認得的名字（LINE 名稱）')
h = h.replace('看預購名單', '看購物清單')
rep('<div class="box"><h3>📝 接龍格式</h3>', '<div class="box"><h3>📝 怎麼跟團</h3>')
h = h.replace('複製貼到群組就完成了！', '複製後私訊貼給芸琪就完成了！')
rep('群組接龍截止', '代購截止')
rep('＋ 加入我的接龍', '＋ 加入購物清單')
rep('本次接龍已截止，感謝大家！', '本次代購已截止，感謝大家！')
open(os.path.join(ROOT, 'yl-bf-friend.html'), 'w', encoding='utf-8').write(h)
left = re.findall(r'[^<>"\'`\n]{0,20}(?:芳療群組|_wPcpU75Jp|接龍)[^<>"\'`\n]{0,20}', re.sub(r'const D=\{.*?\};\n', '', h, flags=re.S))
print('剩下的字：', left)
