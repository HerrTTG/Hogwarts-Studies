import csv
import pyinputplus


class BaseAPI():
    def __init__(self, path):
        print("*****************************")
        print("*      图书管理系统           *")
        print("* 1. 添加新图书信息           *")
        print("* 2. 通过图书ID修改图书信息      *")
        print("* 3. 通过图书ID删除图书信息      *")
        print("* 4. 通过书名删除图书信息      *")
        print("* 5. 通过图书ID查询图书信息      *")
        print("* 6. 通过书名查询图书信息      *")
        print("* 7. 显示所有图书信息         *")
        print("* 8. 退出系统                *")
        print("*****************************")
        self.workpath = path
        self.data = self.load_data()

    def bookManager(self):
        while True:
            select_op = input("输入编号选择操作：")
            if len(select_op) == 1 and select_op in "12345678":
                if select_op == "1":
                    try:
                        sid = self.getSid(select_op)
                        assert sid
                        name = self.getName()
                        price = self.getPrice()
                        assert price
                        summary = self.getSummary()
                    except:
                        print('返回菜单')
                        continue
                    else:
                        self.addBook(sid, name, price, summary)
                elif select_op == "2":
                    sid = self.getSid(select_op)
                    self.modifyBookByID(sid)
                elif select_op == "3":
                    sid = self.getSid(select_op)
                    self.deleteBookByID(sid)
                elif select_op == "4":
                    name = self.getName()
                    self.deleteBookByName(name)
                elif select_op == "5":
                    sid = self.getSid(select_op)
                    self.queryBookByID(sid)
                elif select_op == "6":
                    name = self.getName()
                    self.queryBookByName(name)
                elif select_op == "7":
                    self.showAllInfo()
                else:
                    self.save_data()
                    break

            else:
                print("输入的数据不合法，请输入在合法范围内的操作编号！！！")

    def load_data(self):
        with open(self.workpath + '\CK290520\data\db.csv', 'r', encoding='utf-8') as f:
            fr = list(csv.reader(f))
            # [['编号（sid)', ' 书名（name)', ' 价格（price)', ' 简介（summary)'], ['1', '哈利波特', '10$', '天选之子']]

        colum = fr[0]
        books = fr[1:]
        data = []
        for i in books:
            books_data = {}
            for j in range(4):
                books_data[colum[j]] = i[j]
            else:
                data.append(books_data)
        return data

    def save_data(self):
        with open(self.workpath + '\CK290520\data\db.csv', 'w', encoding='utf-8', newline='') as f:
            outputwriter = csv.writer(f, delimiter=',')
            output = []
            output.append(['编号（sid)', '书名（name)', '价格（price)', '简介（summary)'])
            for i in self.data:
                # {' 书名（name)': 'test', ' 价格（price)': '222', ' 简介（summary)': '123', '编号（sid)': '3'}
                output.append([i['编号（sid)'], i['书名（name)'], i['价格（price)'], i['简介（summary)']])
            outputwriter.writerows(output)

    def check_id(self, sid, select_op, _tmp):

        if select_op == '1':
            try:
                assert int(sid) not in _tmp
            except:
                print('SID重复')
                return False
            else:
                return sid
        else:
            try:
                assert int(sid) in _tmp
            except:
                print('SID不存在')
                return False
            else:
                return sid

    def getSid(self, select_op):
        for j in range(3):
            try:
                sid = pyinputplus.inputNum("请输入图书ID:", limit=3)
            except:
                print('输入错误多次！')
                return False
            else:
                _tmp = []
                for i in self.data:
                    _tmp.append(int(i['编号（sid)']))
                return self.check_id(sid, select_op, _tmp)

    def getName(self):
        name = input("请输入图书书名：")
        return name

    def getPrice(self):
        try:
            price = pyinputplus.inputNum("请输入图书价格：", limit=3)
        except:
            print('输入错误多次！')
            return False
        else:
            return price

    def getSummary(self):
        summary = input("请输入图书简介：")
        return summary
