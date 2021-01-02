import time
import pyautogui

def SendMessage():
    time.sleep(5)
    text = open('message.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')

SendMessage()