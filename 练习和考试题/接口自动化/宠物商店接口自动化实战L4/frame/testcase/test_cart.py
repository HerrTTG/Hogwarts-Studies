import allure
import jsonpath
import logging
import pytest
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
        logging.info(f'环境信息:{envinfo}')

    @allure.feature('宠物商店')
    @allure.story('宠物管理系统')
    @pytest.mark.parametrize('goods_name', ['testhzy1', 'testhzy2'])
    def test_case1(self, envget, goods_name):
        """
        描述测试步骤
        购物车测试
        1.调用添加货品接口，增加一个货品
        2.调用查询接口检查是否添加成功
        3.查询货物详情
        4.调用添加购物车接口，添加到购物车中
        """
        allure.dynamic.title(f'购物车流程测试：货品名称{goods_name}')

        logging.info(f'购物车流程测试：货品名称{goods_name}')

        # 将fixture命令行获取的环境信息，带入到方法中去参与创建对象
        self._preint(envget)

        goods_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "9001",
                      "name": goods_name}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "66", "number": "66", "url": ""}],
            "attributes": []}

        # 用例执行,接口需要的各类参数
        with allure.step(f'测试步骤一：添加商品信息'):
            r1 = self.goods.create(goods_data)

        with allure.step(f'测试步骤二：根据商品名{goods_name}查询list接口'):
            r2 = self.goods.list(goods_name=goods_name, order="desc", sort="add_time")
            self.goods_id = r2.json()["data"]["list"][0]["id"]
            logging.info(f'list 接口获取到的goods_id为{self.goods_id}')

        with allure.step(f'测试步骤三，根据商品id:{self.goods_id}查询详情'):
            r3 = self.goods.detail(self.goods_id)
            self.product_id = r3.json()["data"]["products"][0]["id"]
            logging.info(f'detail 接口获取到的product_id为{self.product_id}')

        with allure.step(f'测试步骤四：根据商品id:{self.goods_id}和产品id:{self.product_id}将产品添加购物车'):
            r4 = self.cart.add(self.goods_id, self.product_id)
            assert jsonpath.jsonpath(r4.json(), '$..errmsg')[0] == "成功"

        # 子类删除方法
        # self.goods.delete(self.goods_id)

        # domin测试
        self.goods.delete_by_name(goods_name)

    def test_other(self):
        pass
    # def teardown(self):
    #     # 由于其他测试用例可能不生成新的goodsid，以及新增添加的goods数据，
    #     # 所以在无法确定后续用例是否需要统一清理一样的内容时，不要使用teardown
    #     # 将删除动作直接写入用例即可
    #    self.goods.delete(self.goods_id)
