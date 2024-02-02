import tkinter as tk
window =tk.Tk()
#设置窗口title
window.title('PythonGUI学习')
#设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
window.geometry('450x300')
# 获取电脑屏幕的大小
print("电脑的分辨率是%dx%d"%(window.winfo_screenwidth(),window.winfo_screenheight()))
# 要求窗口的大小，必须先刷新一下屏幕
window.update()
print("窗口的分辨率是%dx%d"%(window.winfo_width(),window.winfo_height()))
# 如使用该函数则窗口不能被拉伸
# window.resizable(0,0)
# 改变背景颜色
window.config(background="#6fb765")
# 设置窗口处于顶层
window.attributes('-topmost',True)
# 设置窗口的透明度
window.attributes('-alpha',1)
# 设置窗口被允许最大调整的范围，与resizble()冲突
window.maxsize(600,600)
# 设置窗口被允许最小调整的范围，与resizble()冲突
window.minsize(50,50)
#更改左上角窗口的的icon图标,加载C语言中文网logo标
#window.iconbitmap('C:/Users/Administrator/Desktop/favicon.ico')
#添加文本内容,并对字体添加相应的格式 font(字体,字号,"字体类型")
text=tk.Label(window,text="Python学习，网址：https://editor.csdn.net",bg="yellow",fg="red",font=('Times', 15, 'bold italic underline'))
#将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button=tk.Button(window,text="关闭",command=window.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
#进入主循环，显示主窗口
window.mainloop()