import tkinter as tk
#entry就是输入框
#text是一个可编辑的文本框，一般用于输出或者用户进行编辑使用，不作为程序的输入入口。
window=tk.Tk()

window.title('学习entry和text')
window.geometry('400x400')
e=tk.Entry(window,show=None)
t=tk.Text(window,height=3)

def insertp():
    var=e.get()
    t.insert('insert',var)


def endp():
    var=e.get()
    t.insert('end',var)
#insert(1.1,var) 1.1表示插入到第一行第2列    第几行.当前行字符串的什么位置0表示第一位

b1=tk.Button(window,text='Insert point',width=15,height=2,command=insertp)
b2=tk.Button(window,text='insert end',width=15,height=2,command=endp)

#show='*' 输入密码显示为指定符号

e.pack()
t.pack()
b1.pack()
b2.pack()
window.mainloop()
