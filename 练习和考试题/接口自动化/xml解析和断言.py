from requests_xml import XMLSession

session = XMLSession()

r = session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')

# print(r.text)

# 获取xml中的所有link 返回list
# print(r.xml.links)

# 字节形式返回xml
# print(r.xml.raw_xml)

# 具体标签内的内容
# print(r.xml.text)

# 断言 传入xpath表达式来查找
item = r.xml.xpath('//item', first=True)
print(item.text)

# 多个结果查询
items = r.xml.xpath('//link')
results = []
for i in items:
    results.append(i.text)
print(results)
