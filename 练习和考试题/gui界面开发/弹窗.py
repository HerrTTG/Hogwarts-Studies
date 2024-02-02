import tkinter as tk
from tkinter import  messagebox

window=tk.Tk()
window.geometry('400x400')
window.title('弹窗')


def hit_me():
    #messagebox.showinfo(title='Hi',message='hahahahha')
    #messagebox.showwarning(title='Hi', message='nonono')
    #messagebox.showerror(title='Hi', message='holy shit')
    #messagebox.askquestion(title='Hi', message='continu?')  #return yes or no
    #messagebox.askyesno(title='Hi', message='shit drag?') #return True or False
    #messagebox.askretrycancel(title='Hi', message='hahahahha')#return True or False
    #messagebox.askokcancel(title='Hi', message='hahahahha')#return True or False
    messagebox.askyesnocancel(title='Hi', message='hahahahha') #return True or False or None


tk.Button(window,text='hit me',command=hit_me).pack()


window.mainloop()