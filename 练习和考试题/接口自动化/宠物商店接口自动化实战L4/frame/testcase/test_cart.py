import sys

sys.path.append('E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\接口自动化\宠物商店接口自动化实战L4')

from frame.apis.admin.goods import Goods
from frame.apis.wx.cart import Cart
from frame.untils.login import Loginrequest


class Test_cart():

    def preint(self, url):
        """
        初始化实例,同时将token传入进去
        """
        self.url = url
        # 创建登录对象传入需要登录的path和路径
        r = Loginrequest('admin', self.url)
        # 调用gettoken方法，将获取到的token传入到api接口中
        self.token = r.get_token()
        # 创建API接口的调用对象
        self.goods = Goods(self.token)
        self.cart = Cart(self.token)

    def test_case(self, envget):
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
        res = self.goods.list(self.url, goods_name='test', order="desc", sort="add_time")
        # self.goods.detail(self.url)
        # self.cart.add(self.url)
        print(res)
