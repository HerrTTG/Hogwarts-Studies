import  pyautogui,time

wd=pyautogui.getActiveWindow()
wd.minimize()
time.sleep(5)
wd.restore()
time.sleep(5)
wd.minimize()
time.sleep(5)
wd.restore()
#wd.close() 不要轻易使用，可能会跳过某些窗口的自动保存
