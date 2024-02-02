import tkinter as tk


window=tk.Tk()
window.geometry('400x400')
window.title('放置')

#pack grid place

#tk.Label(window,text='test').pack(side='top')
#tk.Label(window,text='test').pack(side='bottom')
#tk.Label(window,text='test').pack(side='left')
#tk.Label(window,text='test').pack(side='right')

#按行列来放置，如四行三列
#for i in range(4):
#    for j in range(3):
#        tk.Label(window, text='123').grid(row=i,column=j,ipadx=10,ipady=10)
#padx pady 是外部扩展的占地字符串面积
#ipadx ipady 是内部扩展的占地字符串面积


tk.Label(window, text='shit drag').place(x=10,y=100,anchor='nw')
#如果是一张图片anchor是用来指定图片的那一个角定位到place的坐标上。如nw西北角，或者说左上角最常用
#放置指定坐标


window.mainloop()

