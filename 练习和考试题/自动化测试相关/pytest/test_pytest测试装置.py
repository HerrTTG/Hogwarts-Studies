class Testcollection():
    # 函数名setup_class / teardown_class	 setup / teardown为固定名称，pytest会自动运行。

    def setup_class(self):
        print('类级开始装置，只在类中用例执行前执行一次，一般用来初始化一些资源。比如数据库连接对象的创建等。')

    def teardown_class(self):
        print('类级结束装置，只在类中用例执行后执行一次,一般用来关闭一些资源。比如浏览器等')

    def setup(self):
        print('方法级开始装置，在每个用例执行前，执行一次。用于初始化用例需要的资源。')

    def teardown(self):
        print('方法级结束装置，在每个用例执行后，执行一次。用于关闭用例需要的资源。')

    def test_demo1(self):
        print('run demo1')

    def test_demo2(self):
        print('run demo2')

    def test_demo3(self):
        print('run demo3')
