import json
import requests
from genson import SchemaBuilder
from jsonschema.validators import validate


# 分装jsonschema，将生成和验证封装为4个方法。
class My_jsonschema():
    @classmethod
    def generate_jsonschema(cls, obj):
        # 实例化SchemaBuilder类
        builder = SchemaBuilder()
        # 调用add_object方法将json数据传入
        builder.add_object(obj)

        # 将schema结果保存为类属性
        cls.schema = builder.to_schema()

    @classmethod
    def generate_jsonschema_file(cls, obj, filepath='./jsonchema.json'):
        # 实例化SchemaBuilder类
        builder = SchemaBuilder()
        # 调用add_object方法将json数据传入
        builder.add_object(obj)
        # 返回为schema格式的json文件
        with open(filepath, 'w') as f:
            json.dump(builder.to_schema(), f)

    @classmethod
    def jsonschema_valida(cls, instobj, schema):
        try:
            validate(instance=instobj, schema=schema)
            return True
        except:
            return False

    @classmethod
    def jsonschema_valida_file(cls, instobj, filepath='./jsonchema.json'):
        with open(filepath, "r") as f:
            schema = json.load(f)
        try:
            validate(instance=instobj, schema=schema)
            return True
        except Exception as e:
            return False


class Test_case():
    def test_case1(self):
        r = requests.request('GET', 'https://httpbin.ceshiren.com/get', verify=False)
        try:
            assert r.status_code == 200
        except:
            raise
        else:
            My_jsonschema().generate_jsonschema(r.json())
            assert My_jsonschema.jsonschema_valida(r.json(), My_jsonschema().schema) == True
