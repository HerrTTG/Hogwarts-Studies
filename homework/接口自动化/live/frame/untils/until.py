import os
import yaml


class Untils():
    @classmethod
    def get_path(cls):
        ## ..\\..\\..\\live
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # print(path)
        return path

    @classmethod
    def get_env(cls, request):
        # 根据命令行获取，从不同的配置文件中获取环境信息
        myenv = request.config.getoption("--env", default='test')
        if myenv == 'test':
            print('获取并返回环境信息，此条为测试环境')
            with open(f'{Untils.get_path()}\\frame\\config\\envtest.yaml', 'r') as file:
                envinfo = yaml.safe_load(file)
        elif myenv == 'dev':
            print('获取并返回环境信息，此条为开发环境')
            with open(f'{Untils.get_path()}\\frame\\config\\devtest.yaml', 'r') as file:
                envinfo = yaml.safe_load(file)
        return envinfo

    @classmethod
    def get_testdata(cls):
        with open(f'{Untils.get_path()}\\frame\\datas\\testdata_departdata.yaml', 'r', encoding='utf-8') as file:
            departdata = yaml.safe_load(file)
        with open(f'{Untils.get_path()}\\frame\\datas\\testdata_memberinfo.yaml', 'r', encoding='utf-8') as file:
            memberinfo = yaml.safe_load(file)
        return departdata, memberinfo
