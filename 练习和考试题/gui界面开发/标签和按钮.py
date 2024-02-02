import tkinter as tk

window=tk.Tk()

window.title('学习标签和按钮')
window.geometry('400x400')

var=tk.StringVar()
l=tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=20,height=2)
#第一个参数指向此标签是在哪个窗口上的

on_hit=False
def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('你点到我了！快撤回！')
    else:
        on_hit = False
        var.set('')

b=tk.Button(window,text='点我',width=15,height=2,command=hit_me)


#安置标签
l.pack()
b.pack()
window.mainloop()