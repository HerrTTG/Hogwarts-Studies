"""
api定义
admin/goods 下的具体接口
"""
import requests


class Goods:

    def __init__(self, url, token):
        self.send = requests.request
        self.url = url
        self.token = token


    def create(self):
        pass

    def list(self, goods_name, order="desc", sort="add_time"):
        """
        封装接口调用的动作
        """
        goods_list_url = self.url + "/admin/goods/list"
        goods_data = {
            "name": goods_name,
            "order": order,
            "sort": sort
        }
        r = self.send("get", goods_list_url, params=goods_data, headers={"X-Litemall-Admin-Token": self.token},
                      verify=False)

        return r.json()

    def detail(self):
        pass
