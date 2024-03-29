#### 安裝所需套件
`pip install -r requirements.txt`

#### 下載圖像辨識軟體 
Tesseract-OCR
- 下載位置:
`https://github.com/UB-Mannheim/tesseract/wiki`
- 下載檔案:
`tesseract-ocr-w64-setup-v5.0.0-alpha.20200328.exe`
- 安裝路徑位置:
`C:\Program Files (x86)\Tesseract-OCR`
- 切換到安裝路徑位置:
`cd C:\Program Files (x86)\Tesseract-OCR`
- 確認是否安裝成功:
`tesseract -v`

#### 程式中需注意內容
- 設置tesseract.exe安裝路徑

`pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'`

- encoding="utf-8": 解決UnicodeDecodeError問題

#### 透過keyboard套件來實作功能
- keyboard.is_pressed(): 判斷是否輸入按鍵

#### 透過pyautogui套件來實作功能
- pyautogui.alert(): 顯示消息視窗 
- pyautogui.position(): 目前滑鼠坐標
- pyautogui.screenshot(): 截圖

#### 透過pytesseract套件來實作功能
- 辨識圖像中的文字並取出

#### 透過google_trans_new套件來實作功能
- 將取出的文字翻譯成繁體字

- 最後將翻譯前與翻譯後的文字寫入txt檔中

#### 程式說明
使用Python語言開發，透過使用者輸入"Z"與"X"鍵來取得欲擷取之圖像範圍，

然而辨識文字來做翻譯處理，最後將結果呈現與寫入文字檔。

#### 執行結果
![image](img/img1.PNG)

![image](img/img2.PNG)

![image](img/img3.PNG)

![image](img/img6.png)

![image](img/img5.PNG)

![image](img/img4.PNG)


