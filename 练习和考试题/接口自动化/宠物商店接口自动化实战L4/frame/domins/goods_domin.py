# 本意是业务的抽象，涉及设计模式，架构等相关知识
# 如果很难理解。作为拔高知识，不要求完全听懂和掌握

# domin的作用是抽象化api，不做具体实现
# 代表某一种业务模型
# 子类继承此父类后，需要实现下述所有涉及到的方法
# 同时domin还可以对子类实现的方法进行重组，生成一个子类没有的方法供其使用
class GoodsDomain:
    def create(self):
        pass

    def list(self):
        pass

    def detail(self):
        pass

    def delete(self):
        pass

    def delete_by_name(self, name):
        """
        demin对子类实现方法的重组
        """
        # 原理是子类继承父类的所有方法，但又会对同名的方法进行重写
        # domin中写的四个同名方法的实现都在子类api中
        # 新增一个delete_by_name方法。并描述他的实现逻辑
        # 此时子类api也就拥有了这个方法
        goods_list_r = self.list(name)
        goods_id = goods_list_r.json()["datas"]["list"][0]["id"]
        self.delete(goods_id)
