'''
pytest的公共数据和方法模块。
将此文件和测试用例py文件放入一个文件夹内即可。
'''
import pytest


# hook函数
# 收集测试用例，收集之后（改编码，改执行顺序）
def pytest_collection_modifyitems(items: list):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    # item中是一个方法对象，此方法对象就是对应的测试用例了
    # name就是测试用例的名字
    # _nodeid测试用例的路径
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


# 给pytest添加自定义命令行参数
def pytest_addoption(parser):
    # parser
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 参数的默认值
                      dest='env',  # 存储的变量，为属性命令，可以使用Option对象访问到这个值，暂用不到
                      help='set your run env'  # 帮助提示 参数的描述信息
                      )


# fixture
@pytest.fixture(scope='session')
def envget(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        print('获取并返回环境信息，此条为测试环境')
        return "https://petstore.swagger.io/v2"
    elif myenv == 'dev':
        print('获取并返回环境信息，此条为开发环境')
        return "https://petstore.swagger.io/v2"


@pytest.fixture(scope='session')
def dataload():
    pet_id = 9223372000001084222
    pet_status = "available"
    add_pet_info = {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "cat"
        },
        "name": "miao",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 5,
                "name": "cute"
            }
        ],
        "status": pet_status
    }
    update_name = "hzy-hogwarts"
    update_pet_info = {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "cat"
        },
        "name": update_name,
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 5,
                "name": "cute"
            }
        ],
        "status": pet_status
    }
    search_param = {
        "status": pet_status
    }

    proxy = {
        "http": "http://127.0.0.1:8888",
        "https": "http://127.0.0.1:8888"
    }

    return pet_id, pet_status, add_pet_info, update_name, update_pet_info, search_param, proxy
