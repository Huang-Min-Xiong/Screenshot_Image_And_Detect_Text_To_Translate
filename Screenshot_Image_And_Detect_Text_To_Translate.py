import keyboard
import pyautogui
import pytesseract
from cv2 import cv2
from google_trans_new import google_translator

#tesseract.exe安裝路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#左上角座標
def Upper_left_corner():
    pyautogui.alert('請移至欲截圖之左上角按下z鍵!')
    while True:
        if keyboard.is_pressed('z'):
            global pos1
            pos1 = pyautogui.position()
            print(pos1)
            break

#右下角座標
def Lower_right_corner():
    pyautogui.alert('請移至欲截圖之右下角按下x鍵!')
    while True:
        if keyboard.is_pressed('x'):
            global pos2
            pos2 = pyautogui.position()
            print(pos2)
            break

#偵測圖像文字且翻譯文字
def Detect_image_text_and_translate():
    img = cv2.imread(r'.\img.png')
    text = pytesseract.image_to_string(img)
    print('翻譯前:\n'+str(text)+'\n')

    translator = google_translator()  
    #,lang_src='en'
    translate_text = translator.translate(text, lang_tgt='zh-TW') #翻譯繁體
    print('翻譯後:\n'+str(translate_text)+'\n')
    pyautogui.alert(translate_text,'翻譯內容')

    with open(r".\Detect_Text.txt","w") as f:
        f.write('翻譯前:\n'+str(text)+'\n\n') #翻譯前寫入文字檔
        f.write('翻譯後:\n'+str(translate_text)+'\n\n') #翻譯後寫入文字檔
        print('已寫入文字檔!')


if __name__ == "__main__":
    Upper_left_corner()
    Lower_right_corner()
    x = pos1.x
    y = pos1.y
    w = pos2.x-pos1.x
    h = pos2.y-pos1.y
    img = pyautogui.screenshot(region=(x,y,w,h))
    img.save(r'.\img.png')
    pyautogui.alert('截圖已成功!')
    Detect_image_text_and_translate()