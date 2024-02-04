'''
作业：
实现学生管理系统：

学生信息包含：
    - 编号（sid), 姓名（name), 年龄（age), 性别（gender) 四个信息
    - 每个学生信息使用字典形式保存
    - 使用列表保存所有学生的信息

1. 实现菜单函数，输出下列信息，返回用户输入的编号，并进行输入校验。

    print("****************************************")
    print("*                                学生管理系统                         *")
    print("*              1. 添加新学生信息              *")
    print("*             2. 通过学号修改学生信息                 *")
    print("*                3. 通过学号删除学生信息                 *")
    print("*                4. 通过姓名删除学生信息                 *")
    print("*             5. 通过学号查询学生信息          *")
    print("*                6. 通过姓名查询学生信息          *")
    print("*                7. 显示所有学生信息             *")
    print("*                8. 退出系统                                           *")
    print("****************************************")
    select_op = input("输入编号选择操作：")

2. 实现控制函数，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
3. 实现添加学生函数，函数参数为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
4. 实现修改函数，参数为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功
5. 实现删除函数，参数为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
6. 实现删除函数，参数为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
7. 实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
8. 实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
9. 实现函数，输出所有学生信息
'''
'''
I: opcode，编号 学号 姓名 年龄 性别  
P:实现控制，用来控制菜单的输出与功能的选择，直到用户选择8，结束程序运行。
  实现信息添加，入参为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。
  实现修改函数，入参为学号，如果学生存在，则进行修改，不存在输出提示，并返回是否修改成功。
  实现删除函数，入参为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
  实现删除函数，入参为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，并返回是否删除成功
  实现查询函数，入参为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
  实现查询函数，入参为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
  无入参，输出所有学生信息
O: 参考P中的要求 
'''

import os
import time

import pyinputplus


class Managementsystem:

    @classmethod
    def intro(cls):
        """界面展示，参与无限循环。用类方法来调用，不限制对象"""
        print("****************************************")
        print("*            学生管理系统                *")
        print("*         1. 添加新学生信息               *")
        print("*         2. 通过学号修改学生信息          *")
        print("*         3. 通过学号删除学生信息          *")
        print("*         4. 通过姓名删除学生信息          *")
        print("*         5. 通过学号查询学生信息          *")
        print("*         6. 通过姓名查询学生信息          *")
        print("*         7. 显示所有学生信息             *")
        print("*         8. 退出系统(保存变更)           *")
        print("*         0. 取消变更                   *")
        print("****************************************")

    def start(self,):
        """系统初始化，根据数据的opcode将对应的信息写入对象的属性中。并且会区分opcode的业务而排除不需要的数据输入"""
        try:
            self.opcode=pyinputplus.inputInt('请输出操作方式:',min=0,max=8,limit=3)
            assert self.opcode !=8
        except:
            print('程序退出...')
            time.sleep(2)
        else:
            if self.opcode==1:
                self.num=str(pyinputplus.inputInt('请输入编号(从1开始):',min=1,limit=3))
                self.sid=str(pyinputplus.inputInt('请输入学号:',limit=3))
                self.name=str(input('请输入姓名:'))
                self.age=str(pyinputplus.inputInt('请输入年龄:',min=1,limit=3))
                self.gender = str(pyinputplus.inputChoice(['Man', 'Lady', 'NA'], prompt='请输入性别(Man or Lady or NA):'))
            elif self.opcode==2:
                self.sid = str(pyinputplus.inputInt('请输入学号:', limit=3))
                self.num=str(pyinputplus.inputInt('请输入编号(从1开始):',min=1,limit=3))
                self.name = str(input('请输入姓名:'))
                self.age=str(pyinputplus.inputInt('请输入年龄:',min=1,limit=3))
                self.gender = str(pyinputplus.inputChoice(['Man', 'Lady', 'NA'], prompt='请输入性别(Man or Lady or NA):'))
            elif self.opcode in [3,5]:
                self.sid=str(pyinputplus.inputInt('请输入学号:',limit=3))
            elif self.opcode in [4,6]:
                self.name=str(input('请输入姓名:'))
            elif self.opcode ==7:
                self.name='***'



class Operationsystem(Managementsystem):
    def readdata(self):
        """读取或者建立数据文件，进入循环前或者opcode为0时运行。保证对象属性self.ls的最时效性
           本地数据文本采用csv格式"""
        self.ls=[]
        if os.path.isfile('./data.csv'):
            with open('./data.csv','r',encoding='utf-8') as f:
                for i in f.readlines():
                    # f.readlines将返回所有行，每一行作为一个单独的元素形成的list
                    # 循环遍历这个list 变量i,此时就代表是每一行的字符串如'编号,学号,姓名,年龄,性别\n'
                    i=i.replace('\n','')
                    #去除小尾巴
                    self.ls.append(i.split(','))
                    #将字符串i 按照,分割为一个list 在加入self.ls中。形成一个二维的列表
                #print(self.ls)
        else:
            with open('./data.csv','w',encoding='utf-8') as f:
                f.write('编号,学号,姓名,年龄,性别\n')
    def selectmune(self):
        """菜单多态方法，根据opcode的不同，返回不同的类方法名。注意是返回方法名，而不进行调用.
           此举是为了再次判断opcode是否为8,如果为8,执行保存退出操作.在返回false,使大循环break"""
        if self.opcode==8:
            Operationsystem.autoexit(self)
            return False
        else:
            d={1:self.add,2:self.modify,3:self.dele,
                4:self.dele,5:self.search,6:self.search,7:self.search,0:self.cancle}
            return d[self.opcode]

    def cancle(self):
        """取消任何数据变更方法，对应opcode==0  本质就是刷新self.ls 再去读取当前数据文件一次"""
        self.readdata()
        print('取消所有变更成功')
        time.sleep(2)

    @classmethod
    def autoexit(cls,self):
        """名虽autoexit，但不aoto。当opcode为8时会从菜单方法中被调用。检查self.ls是否有数据，即是否被读取或者修改过。
           将self.ls的数据覆盖到本地文本中"""
        if self.opcode == 8 and len(self.ls)>=1:
            fo=open('./data.csv', 'w', encoding='utf-8')
            for i in self.ls:
                fo.writelines(','.join(i)+'\n')
                # 与读取时同理，i 变量为self.ls中的每一个元素，即每一行形成的一维列表。
                # ','.join(i) 表示用逗号作为分隔符在每一个元素之间，从i列表中。返回的是一个字符串即'编号,学号,姓名,年龄,性别'
                # 最后加上小尾巴
                # writelines按行写入。
                #小TIP:join里面传入的一定是个一个可迭代对象。
            fo.close()

    def add(self):
        '''实现信息添加，入参为编号，姓名，年龄，性别四个参数，返回是否添加成功的结果，要求编号不可重复。'''
        try:
            if len(self.ls)>1:
                for i in self.ls[1:]:
                    assert i[0]!=self.num,'编号必须不等于已有编号 否则异常退出'
                    assert i[1] != self.sid, '学号必须不等于已有学号 否则异常退出'
        except:
            print('重复的唯一标识码，请检查学号或者编号是否已在系统中存在！')
            time.sleep(3)
        else:
            self.ls.append([self.num,self.sid,self.name,self.age,self.gender])
            print('添加成功')
            time.sleep(3)


    def modify(self):
        '''实现修改函数，入参为学号，如果学生存在，则进行修改，不存在输出提示，并返修改结果'''
        if len(self.ls)>1:
            for i in range(len(self.ls)):
                if self.ls[i][1]==self.sid:
                    self.ls[i]=[self.num,self.sid,self.name,self.age,self.gender]
                    print('修改成功')
                    time.sleep(3)
                    break
            else:
                print('未找到学生学号')
                time.sleep(3)

        else:
            print('系统数据为空，请直接添加')
            time.sleep(3)
    def dele(self):
        '''  实现删除函数，入参为学号，如果学生存在，则进行删除，不存在输出提示，并返回是否删除成功
             实现删除函数，入参为姓名，如果学生存在，则进行删除（同名学生全部删除），不存在输出提示，'''
        if len(self.ls)>1:
            if self.opcode == 3:
                #通过学号删除
                for i in range(len(self.ls)):
                    if self.ls[i][1] == self.sid:
                        del self.ls[i]
                        print('删除成功')
                        time.sleep(3)
                        break
                else:
                    print('未找到学生学号')
                    time.sleep(3)
            else:
                # 通过姓名删除全部同名
                ls=[]
                for item in self.ls:
                    if  item[2]==self.name:
                        ls.append(item)
                else:
                    if len(ls)<1:
                        print(f'未找到{self.name}学生')
                        time.sleep(3)
                    else:
                        for i in ls:
                            self.ls.remove(i)
                        print(f'删除所有{self.name}的学生成功')
                        time.sleep(3)
        else:
            print('系统数据为空，无法进行删除数据操作')
            time.sleep(3)

    def search(self):
        '''实现查询函数，参数为学号，如果学生存在，则输出学生信息，不存在输出提示，并返回是否查询成功
           实现查询函数，参数为姓名，如果学生存在，则输出学生信息（同名学生全部输出），不存在输出提示，并返回是否删除成功
           实现函数，输出所有学生信息'''
        if self.opcode==5:
            for item in self.ls:
                if item[1]==self.sid:
                    print(self.ls[0],end='\n')
                    print(item)
                    time.sleep(3)
                    break
            else:
                print(f'未找到学号{self.sid}的学生信息')
                time.sleep(3)
        elif self.opcode==6:
            ls=[]
            for item in self.ls:
                if item[2]==self.name:
                    ls.append(item)
            else:
                try:
                    assert len(ls)>=1
                except:
                    print(f'未找到姓名{self.name}的学生信息')
                    time.sleep(3)
                else:
                    print(self.ls[0])
                    for i in ls:
                        print(i)
                    time.sleep(3)
        else:
            for item in self.ls:
                print(item)
                time.sleep(3)


if __name__=='__main__':
    a = Operationsystem()
    a.readdata()
    while True:
        Managementsystem.intro()
        a.start()
        b=a.selectmune()
        if b:  # 只要不是8 返回的就是对应的函数名，8 会返回False 导致进入esle中触发break
            b()
        else:
            break
