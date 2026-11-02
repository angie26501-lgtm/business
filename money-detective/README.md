# 人生金錢偵探社｜家庭財務長養成航記（專案目錄）

總目錄（建議加書籤）：https://angie26501-lgtm.github.io/business/money-detective/catalog.html

| 檔案 | 用途 | 對象 |
|---|---|---|
| `index.html` | 財富航海群島：8 座島、31 案、驗收小遊戲、登船通行碼、逐島解鎖 | 學員（對外） |
| `admin.html` | 成員學習進度（管理者，需管理密碼） | Angie |
| `progress-script.gs` | 進度資料庫 Apps Script（部署後網址填進 index.html、admin.html 的 `PROGRESS_URL`；管理密碼只填在 Apps Script，不推上 GitHub） | Angie |
| `catalog.html` | 總目錄：所有頁面入口與各島直連 | Angie／學員 |
| `scripts.html` | 31 案短影音腳本包 | 內部製作 |
| `prompts.html` | ChatGPT 情境圖指示詞（總覽＋8 島） | 內部製作 |
| `hero.jpg` | 主視覺 | — |
| `img/s1.jpg`～`s8.jpg` | 各島情境圖（8 島齊全） | — |

- 直接開某座島：`index.html#s1` ～ `#s8`
- 營隊任務進度：`index.html#camp3`（三日營，資料在 `CAMP3`）、`index.html#camp5`（五日營，資料在 `CAMP`）；逐日解鎖、完成可複習
- 五日營專用通行碼：`綠芽五日營`（只參加五日營的夥伴輸入後，不用完成三日營就能打開五日營任務；改碼請改 `index.html` 裡的 `C5_CODE`）
- 登船通行碼：`綠芽登島`（改碼請改 `index.html` 裡的 `PASS_CODE`）；學員填「登島問卷」後自動取得
- 新增島嶼圖片：放進 `img/` 並在 `index.html` 的 `IMGS` 加上對應檔名
- 影片連結：填在 `index.html` 裡每案的 `link` 欄位
- Angie｜家族傳承生活顧問
