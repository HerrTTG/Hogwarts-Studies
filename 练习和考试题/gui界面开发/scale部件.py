import tkinter as tk
#生成的是一个可拉动的进度条
window=tk.Tk()
window.geometry('400x400')
window.title('学习scale部件')



l=tk.Label(window,bg='yellow',width=20,text='')

def print_select(v):
    l.config(text='you have select '+v)


s=tk.Scale(window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,length=200,\
           showvalue=False,tickinterval=3,resolution=0.01,command=print_select)

l.pack()
s.pack()
window.mainloop()
#label可拖动条的名字
#orient=tk.HORIZONTAL 来设置为横向 纵向VERTICAL
#showvalue=False 拖选的数是否展示
#tickinterval=3  下标尺的刻度
#resolution=0.01 保留几位小数
#Scale会默认传值进入command调用的函数里
