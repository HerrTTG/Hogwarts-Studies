import tkinter as tk
#生成的是一个可拉动的进度条
window=tk.Tk()
window.geometry('400x400')
window.title('学习多选部件')


l=tk.Label(window,bg='yellow',width=20,text='')

def print_select():
    dict={'00':' i dont love both','01':'i love C++','10':'I love Python','11':'i love both'}
    l.config(text=dict[str(var1.get())+str(var2.get())])


var1=tk.IntVar()
var2=tk.IntVar()
c1=tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,command=print_select)
c2=tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,command=print_select)

l.pack()
c1.pack()
c2.pack()

window.mainloop()