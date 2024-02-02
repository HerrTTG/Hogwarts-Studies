import tkinter as tk

window=tk.Tk()
window.geometry('400x400')
window.title('学习菜单按钮')

l=tk.Label(window,bg='yellow')
menu=tk.Menu(window)
#定义一个菜单对象
filemenu=tk.Menu(menu,tearoff=0)
#定义菜单对象的第一个可选项的对象
#tearoff是否能分开
menu.add_cascade(label='filemenu',menu=filemenu)
#将第一个可选项串流到menu对象中
count=0
def do_job():
    global count
    l.config(text='do'+str(count))
    count+=1

filemenu.add_command(label='New file',command=do_job)
#给可选项定义可选的标签以及执行的动作
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
#分隔符
filemenu.add_command(label='Quit',command=window.quit)
'''
New file
Open
Save
——————
Quit
'''

editmenu=tk.Menu(menu,tearoff=0)
#定义第二个可选项对象
menu.add_cascade(label='edit',menu=editmenu)
#串流第二个可选项到菜单对象
editmenu.add_command(label='edit file',command=do_job)
editmenu.add_command(label='cut',command=do_job)
editmenu.add_command(label='copy',command=do_job)

submune=tk.Menu(editmenu,tearoff=0)
#在定义子菜单，指向的master位第二个可选项对象editmenu
editmenu.add_cascade(label='import',menu=submune,underline=0)
#串流，并定义标签为import
submune.add_command(label='submune1',command=do_job)
#添加执行功能

l.pack()
window.config(menu=menu)
#配置窗口的菜单 指向为创建的menu对象
window.mainloop()