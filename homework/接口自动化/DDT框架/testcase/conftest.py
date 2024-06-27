# 利用pytest hook机制在查找文件的时候分析测试用例文件
from collecter.yaml_file import YamlFile


# 利用pytest的hook函数，来获取所有的yaml文件。分析测试用例
def pytest_collect_file(parent, file_path):
    # 寻找所有的test_*.yaml的文件
    if file_path.suffix == ".yaml" and file_path.name.startswith("test"):
        # 返回一个有效的对象则会被pytest当做一个测试集
        return YamlFile.from_parent(parent, path=file_path)
