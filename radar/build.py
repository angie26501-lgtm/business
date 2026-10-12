"""壽險商品雷達：把 data/*.json 內嵌進 index.html（單檔、免連網即可查詢）。
用法：python3 build.py
data/ 每個公司一個檔：{company, updated, items:[...]}；data/_meta.json：{last_run, log:[{date,text}]}
"""
import json, glob, os
here = os.path.dirname(os.path.abspath(__file__))
docs = []
for f in sorted(glob.glob(os.path.join(here, "data", "*.json"))):
    if os.path.basename(f).startswith("_"):
        continue
    docs.append(json.load(open(f, encoding="utf-8")))
meta = json.load(open(os.path.join(here, "data", "_meta.json"), encoding="utf-8"))
payload = json.dumps({"docs": docs, "last_run": meta["last_run"], "log": meta.get("log", [])[:60]},
                     ensure_ascii=False).replace("</", "<\\/")
tpl = open(os.path.join(here, "template.html"), encoding="utf-8").read()
open(os.path.join(here, "index.html"), "w", encoding="utf-8").write(tpl.replace("__DATA__", payload))
print("商品數", sum(len(d["items"]) for d in docs), "公司數", len(docs))
