import json
from genson import SchemaBuilder
from jsonschema.validators import validate


def generate_jsonschema(obj):
    # 实例化SchemaBuilder类
    builder = SchemaBuilder()
    # 调用add_object方法将json数据传入
    builder.add_object(obj)
    # 返回为schema格式
    return builder.to_schema()


def jsonschema_valida(instobj, schema):
    try:
        validate(instance=instobj, schema=schema)
        return True
    except:
        return False


def generate_jsonschema_file(obj):
    # 实例化SchemaBuilder类
    builder = SchemaBuilder()
    # 调用add_object方法将json数据传入
    builder.add_object(obj)
    # 返回为schema格式的json文件
    with open('./jsonchema.json', 'w') as f:
        json.dump(builder.to_schema(), f)


def jsonschema_valida_file(instobj, filepath):
    with open(filepath, "r") as f:
        schema = json.load(f)
    try:
        validate(instance=instobj, schema=schema)
        return True
    except Exception as e:
        return False


print(generate_jsonschema({'test': 1123}))
print(jsonschema_valida({'test': 1123}, generate_jsonschema({'test': 1123})))
generate_jsonschema_file({'test': 1123})
print(jsonschema_valida_file({'test': 'ad'}, './jsonchema.json'))
