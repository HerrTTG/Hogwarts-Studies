import json

# 序列化就是将python数据转化为json

# 定义一个Python字典
data = {
    "code": 200,
    "msg": "success",
    "datas": [
        {
            "goods_id": "g0001",
            "goods_name": "iPhone12",
            "goods_price": 6999,
            "is_use": True
        },
        {
            "goods_id": "g0002",
            "goods_name": "iPhone13",
            "goods_price": 7999,
            "is_use": False
        }

    ]
}

# 将Python程序中的数据序列化为JSON格式的字符串
json_str = json.dumps(data)
print(json_str)
# True 和false因为json格式为小写 会从pyton的的大些变为小写

# with open('.\webdata.json','w') as f :
#     f.write(json_str)


# 简化写法：

with open('.\webdata.json', 'w') as file:
    json.dump(data, file)
