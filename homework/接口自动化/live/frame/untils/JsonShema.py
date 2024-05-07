import json
from frame.untils.until import Untils
from genson import SchemaBuilder
from jsonschema.validators import validate


class My_jsonschema():
    """
    封装的jsonschema工具
    """

    @classmethod
    def generate_jsonschema(cls, obj):
        """
        根据传入的obj，生成shema格式数据。
        保存在类属性cls.schema中
        """

        # 实例化SchemaBuilder类
        builder = SchemaBuilder()
        # 调用add_object方法将json数据传入
        builder.add_object(obj)

        # 将schema结果保存为类属性
        cls.schema = builder.to_schema()

    @classmethod
    def generate_jsonschema_file(cls, obj, filepath=f'{Untils.get_path()}\\frame\\config\\jsonchema.json'):
        """
            根据传入的obj，生成shema格式数据。
            保存为文件。
        """

        # 实例化SchemaBuilder类
        builder = SchemaBuilder()
        # 调用add_object方法将json数据传入
        builder.add_object(obj)
        # 返回为schema格式的json文件
        with open(filepath, 'w') as f:
            json.dump(builder.to_schema(), f)

    @classmethod
    def jsonschema_valida(cls, obj, schema):
        """
            根据传入的obj,和schema格式数据，进行断言判断。
            返回bool值。
        """

        try:
            validate(instance=obj, schema=schema)
            return True
        except:
            return False

    @classmethod
    def jsonschema_valida_file(cls, instobj, filepath=f'{Untils.get_path()}\\frame\\config\\jsonchema.json'):
        """
            根据传入的obj,和读取文件中的schema格式数据，进行断言判断。
            返回bool值。
        """
        with open(filepath, "r") as f:
            schema = json.load(f)
        try:
            validate(instance=instobj, schema=schema)
            return True
        except Exception as e:
            return False
