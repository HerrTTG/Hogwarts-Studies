import json

# 记得要用单引号 因为json里面的字符串都是双引号，所以外面要用单引号 或者三引号来区分
json_str = '''{"code": 200, "msg": "success", "data": [{"goods_id": "g0001", "goods_name": "iPhone12", "goods_price": 6999, "is_use": true}, {"goods_id": "g0002", "goods_name": "iPhone13", "goods_price": 7999, "is_use": false}]}'''

# json是字符串，
print(json_str[2])
# 转换为程序数据后，就可以用字典的方式访问里面的数据了
print(json.loads(json_str)['code'])

# 例如从web上获取的json 下来一定是个文本，即字符串。反序列化就是将json变为程序可读的数据格式。方便后续的数据处理。


# 文本反序列化
with open('.\webdata.json', 'r') as file:
    json_file_content = json.load(file)
print(json_file_content['msg'])
