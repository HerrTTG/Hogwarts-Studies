import tkinter as tk
#Radiobutton生成的是一个可选的按钮，多个Radiobutton对象一起放置组成可选项
window=tk.Tk()
window.geometry('400x400')
window.title('学习可选按钮')


var=tk.StringVar()
l=tk.Label(window,bg='yellow',width=15,text='')

def print_select():
    l.config(text='you have select '+var.get())

r1=tk.Radiobutton(window,text='Option A',variable=var,value='A',command=print_select)
r2=tk.Radiobutton(window,text='Option B',variable=var,value='B',command=print_select)
r3=tk.Radiobutton(window,text='Option C',variable=var,value='C',command=print_select)
#value='A' 就是将变量var 赋值A

l.pack()
r1.pack()
r2.pack()
r3.pack()
window.mainloop()