import jsonpath
import requests

data = {
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}

r = requests.request("POST", 'https://httpbin.ceshiren.com/post', json=data, verify=False)

# 使用jsonpath来解析json返回体
# 包括响应体也可以用这种方式

# 对象=jsonpath.jsonpath(json格式内容input,"表达式")
# 对象将被返回查询到的结果数组

responsejs = jsonpath.jsonpath(r.json(), "$..User-Agent")
print(responsejs, r.json()["headers"]["User-Agent"])

# 对消息体进行解析就更加容易
responsejs1 = jsonpath.jsonpath(r.json(), "$..book")
print(responsejs1)

# 更复杂的解析和断言就更需要jsonpath来支持了
responsejs2 = jsonpath.jsonpath(r.json(), "$..book[?(@.title == 'Moby Dick')].price")
assert responsejs2[0] == 8.99
