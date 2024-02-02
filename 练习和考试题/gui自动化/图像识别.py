import pyautogui
from pyautogui import  ImageNotFoundException
try:
    b=pyautogui.locateOnScreen('C:\\Users\\96436\\Desktop\\微信截图_20231226094835.png')
    print(b)
except ImageNotFoundException:
    print('Not found')