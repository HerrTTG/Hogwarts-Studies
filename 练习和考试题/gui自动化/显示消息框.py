import pyautogui


pyautogui.alert('test is ok ','第二个参数是窗口标题') #弹窗并且有个确定按钮
print(pyautogui.confirm('Yes or no?'))#弹窗并且有确定和取消按钮，根据点击结果返回OK 或者 Cancel
pyautogui.prompt('请输入账户：')#弹窗，并有个一个文本字段提供用户输入，以字符串形式返回
pyautogui.password('请输入密码:')

