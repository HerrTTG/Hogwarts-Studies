import sys

sys.path.append('E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\接口自动化\宠物商店接口自动化实战L4')

from frame.apis.admin.goods import Goods
from frame.apis.wx.cart import Cart
from frame.untils.login import Loginrequest


class Test_cart():

    def preint(self, url):
        """
        对不同环境获取到的url根据用例需要的获取不同的token
        对用例的各种请求进行对象创建对象
        """

        # 创建登录对象传入需要登录的path和路径
        ra = Loginrequest('admin', url)
        rc = Loginrequest('wx', url)

        # 创建API接口的调用对象
        self.goods = Goods(url, ra.get_token())
        self.cart = Cart(url, rc.get_token())

    def test_case1(self, envget):
        """
        描述测试步骤
        购物车测试
        1.调用添加货品接口，增加一个货品
        2.调用查询接口检查是否添加成功
        3.查询货物详情
        4.调用添加购物车接口，添加到购物车中
        """
        # 将fixture命令行获取的环境信息，带入到方法中去参与创建对象
        self.preint(envget)

        # 用例执行,传入url和接口需要的各类参数
        # self.goods.create(self.url,goods_name='test',order="desc", sort="add_time")
        res = self.goods.list(goods_name='test', order="desc", sort="add_time")
        # self.goods.detail(self.url)
        # self.cart.add(self.url)
        print(res)
