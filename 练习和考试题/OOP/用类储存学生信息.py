class Student:
    def __init__(self,name,age,sex,pice):
        self.name=name
        self.age=age
        self.sex=sex
        self.pice=pice

    def getinfo(self):
        print(self.name,self.age,self.sex,self.pice)


def main():
    s=''
    ls=[]
    i=1
    lst=[]
    while True:
        s=input(f'请输入第{i}位学生的成绩(输入为空退出):')
        if s=='':
            break
        else:
            ls.append(s.split('#'))
            #每个学生即一个独立的对象，实例化时构造函数构造不同的属性
            stu=Student(ls[i-1][0],ls[i-1][1],ls[i-1][2],ls[i-1][3])
            lst.append(stu)
            i+=1

    for i in lst:
        i.getinfo()







if __name__ =='__main__':
    main()
