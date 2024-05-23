from CK290520.func.Basefunc import Basefunc


class Books(Basefunc):

    def addBook(self, sid, name, price, summary):
        try:
            self.data.append(
                {'编号（sid)': str(sid), '书名（name)': name, '价格（price)': str(price), '简介（summary)': summary})
        except:
            print('添加失败')
        else:
            print('添加成功')

    def modifyBookByID(self, sid):
        for i in range(len(self.data)):
            if int(self.data[i]['编号（sid)']) == sid:
                try:
                    name = self.getName()
                    price = self.getPrice()
                    assert price
                    summary = self.getSummary()
                except:
                    print('返回菜单')
                    break
                else:
                    self.data[i]['书名（name)'] = name
                    self.data[i]['价格（price)'] = str(price)
                    self.data[i]['简介（summary)'] = summary

    def deleteBookByID(self, sid):
        for i in range(len(self.data)):
            if int(self.data[i]['编号（sid)']) == sid:
                try:
                    self.data.pop(i)
                except:
                    print('删除失败')
                else:
                    print('删除成功')
                    break

    def deleteBookByName(self, name):
        _tmp = []
        for i in self.data:
            if i['书名（name)'] == name:
                _tmp.append(i)
        try:
            assert _tmp != []
        except:
            print('删除失败')
        else:
            for j in _tmp:
                self.data.remove(j)
            print('删除成功')


    def queryBookByID(self, sid):
        for i in self.data:
            if int(i['编号（sid)']) == sid:
                print(i)
                break
        else:
            print(f'未查询到编号为{sid}的信息')

    def queryBookByName(self, name):
        ls = []
        for i in self.data:
            if i['书名（name)'] == name:
                ls.append(i)
        else:
            if ls != []:
                for j in ls:
                    print(j)
            else:
                print(f'未查询到书名为{name}的信息')

    def showAllInfo(self):
        for i in self.data:
            print(i)
