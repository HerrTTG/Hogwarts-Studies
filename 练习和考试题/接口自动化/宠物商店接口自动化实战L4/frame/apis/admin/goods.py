"""
api定义
admin/goods 下的具体接口
"""
from frame.apis.BaseAPI import BaseAPI


class Goods(BaseAPI):
    """
    继承父类的构造函数和send方法
    此类为good路径下所有API接口的具体实现描述
    """

    def create(self):
        pass

    def list(self, goods_name, order="desc", sort="add_time"):
        """
        调用只传递必要的接口参数，请求方法和url都不向外体现
        """
        # 根据构造函数实例化的url拼装请求路径
        goods_list_url = self.url + "/admin/goods/list"

        #准备参数信息
        goods_data = {
            "name": goods_name,
            "order": order,
            "sort": sort
        }
        r = self.send("GET", goods_list_url, params=goods_data, verify=False)

        return r

    def detail(self):
        pass
