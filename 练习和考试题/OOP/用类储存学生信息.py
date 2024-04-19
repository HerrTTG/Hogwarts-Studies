# 用类属性来储存每一个独立对象的相关属性
# 创建一个学生类,每个学生都应该有name,age,gender,score属性。
# 定义类在被构造的时候设置赋值类属性。
# 并定义一个类方法，用于访问类属性


class Student:
    def __init__(self, name, age, gender, score):
        self.name=name
        self.age= age
        self.gender = gender
        self.score = score

    def getinfo(self):
        print(self.name, self.age, self.gender, self.score)


def main():
    s=''
    ls=[]
    i=1
    lst=[]
    while True:
        s = input(f'请输入第{i}位学生的成绩(格式:name#age#gender#score,输入为空退出):')
        if s=='':
            break
        else:
            ls.append(s.split('#'))
            #每个学生即一个独立的对象，实例化时构造函数构造不同的属性
            stuobj = Student(*ls[i - 1])
            # 将对象加入一个可迭代容器中
            lst.append(stuobj)
            i += 1

    #遍历容器中的学生对象，调用它的方法获取它的类属性
    for i in lst:
        i.getinfo()







if __name__ =='__main__':
    main()
