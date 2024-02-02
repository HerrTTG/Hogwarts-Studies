import  pyautogui,time


wd=pyautogui.getAllWindows()
for i in wd:
    if str(i.title) == '微信':
        i.activate()
        i.maximize()
        time.sleep(5)
        i.restore()
        i.minimize()