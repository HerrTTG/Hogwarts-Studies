import requests
import xml.etree.ElementTree as ET

r = requests.request("GET", 'https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss', verify=False)
# 返回结果为XML格式响应体
# print(r.text)

# 自己封装XML解析方法
root = ET.fromstring(r.text)

# 查找根元素,根元素是一个元素对象
item = root.findall(".")
# print(item)

# 查找子元素，将xpath表达式写入。items为找到的所有符合条件的子元素列表
items = root.findall(".//link")
# print(items)
for i in items:
    print(i.text)
