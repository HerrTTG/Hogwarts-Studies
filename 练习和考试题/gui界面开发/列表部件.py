import tkinter as tk
#list部件实现展示一个列表，可以共进行选择，点击按钮后输出到标签中
window=tk.Tk()
window.geometry('400x400')
window.title('学习列表部件以及如何获取选定的值')

var1=tk.StringVar()
l=tk.Label(window,bg='yellow',width=4,textvariable=var1)
def pseletion():
    var1.set(listbox.get(listbox.curselection()))
    # listbox.curselection()表示光标所选的元素，再用get方法取出值



b=tk.Button(window,text='print seletion',width=15,height=2,command=pseletion)

var2=tk.StringVar()
var2.set([11,22,33,44])
#设置列表默认值
listbox=tk.Listbox(window,listvariable=var2)

#插入元素到列表
list_items=['first','time']
for item in list_items:
    listbox.insert('end',item)
listbox.insert(1,'first')
listbox.delete(1)


l.pack()
listbox.pack()
b.pack()
window.mainloop()