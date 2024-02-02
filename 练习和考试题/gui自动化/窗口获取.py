import  pyautogui


wd=pyautogui.getAllWindows()
for i in wd:
    print(i.title)