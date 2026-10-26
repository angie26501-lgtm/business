# 綠芽＋五日實踐營 報名頁｜上架說明（給 Codex）

## 要做的事
把這個資料夾 `greensprout/` 整個放進 GitHub repo **angie26501-lgtm/business** 的根目錄，commit 後 push 到 main。

完成後網址會是：
https://angie26501-lgtm.github.io/business/greensprout/

（如果要放在別的 repo 或路徑，請一併修改 index.html 開頭兩行 `og:image`、`og:url` 的網址，LINE／FB 分享預覽圖才會正確。）

## 資料夾內容
| 檔案 | 用途 |
|---|---|
| index.html | 報名頁本體（單檔，無外部 CDN） |
| poster.jpg | 頁首海報，也是 LINE／FB 分享預覽圖 |
| videos/intro.mp4、intro.jpg | 綠芽的初心（芸琪本人配音，71 秒）＋封面 |
| videos/doctor.mp4、doctor.jpg | 小綠芽×芸琪 財務也要看醫生（62 秒）＋封面 |
| videos/story01–04.mp4、.jpg | 人生金錢偵探 動畫短片 4 支＋封面 |

影片都已壓成 720p、加 faststart，最大一支約 6.7 MB，整個資料夾約 28 MB，不需要 Git LFS。

## 頁面重點（請勿更動）
- 所有「傳『綠芽』給芸琪，領優惠碼」按鈕都連到芸琪 LINE@ 一對一：https://lin.ee/8ipLGMe
- 頁面不公開優惠碼／推薦碼，優惠碼由芸琪私訊提供。
- 影片點了才載入（不會拖慢開頁速度），同時只播一支。

## 上架後請檢查
1. 用手機打開網址，海報、價格、五天主題、影片都正常顯示。
2. 點任一支影片能播放、有聲音。
3. 綠色按鈕能開啟 LINE。
4. 把網址貼到 LINE 對話，預覽圖是海報。
