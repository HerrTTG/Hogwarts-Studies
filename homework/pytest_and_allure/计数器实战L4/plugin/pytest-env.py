# 给pytest添加自定义命令行参数插件
def pytest_addoption(parser):
    # parser
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 参数的默认值
                      dest='env',  # 存储的变量，为属性命令，可以使用Option对象访问到这个值，暂用不到
                      help='set your run env'  # 帮助提示 参数的描述信息
                      )
