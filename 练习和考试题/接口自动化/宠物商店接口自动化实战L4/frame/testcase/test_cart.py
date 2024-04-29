import sys
sys.path.append('E:\霍格沃茨学社\Hogwarts-Studies\练习和考试题\接口自动化\宠物商店接口自动化实战L4')

from frame.apis.admin.goods import Goods
from frame.apis.wx.cart import Cart

class Test_cart():

    def _preint(self, envinfo):
        """
        根据接口特性，传递不同的role以获取登录token
        将环境信息文件获取到的信息传入API的实例化过程中去。
        """
        # 创建API接口的调用对象
        self.goods = Goods('admin', envinfo)
        self.cart = Cart('wx', envinfo)

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
        self._preint(envget)

        # 用例执行,接口需要的各类参数
        # self.goods.create(goods_name='test',order="desc", sort="add_time")
        res = self.goods.list(goods_name='test', order="desc", sort="add_time")
        # self.goods.detail()
        # self.cart.add()
        print(res.json())
