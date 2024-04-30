import json
from genson import SchemaBuilder
from jsonschema.validators import validate


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
    def generate_jsonschema_file(cls, obj, filepath='../config/jsonchema.json'):
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
    def jsonschema_valida_file(cls, instobj, filepath='../config/jsonchema.json'):
        with open(filepath, "r") as f:
            schema = json.load(f)
        try:
            validate(instance=instobj, schema=schema)
            return True
        except Exception as e:
            return False
