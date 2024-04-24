from requests_xml import XMLSession

# XML解析主要用于对XML类型返回的消息体进行断言。
# 主要依赖于request_xml中的XMLSession库


# 使用方法：
# 第一步，构造一个对象
session = XMLSession()

# 第二步，类似于request请求，使用对象调用请求方法，对URL进行请求
r = session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss', verify=False)

# #第三步，断言XML内容
#
# # 打印返回的消息体（XML格式）
# print(r.text)
#
# # 获取xml中的所有link，结果为list
# print(r.xml.links)
#
# # 字节形式返回xml
# print(r.xml.raw_xml)
#
# # 返回所有标签内的内容
# print(r.xml.text)
#
# # 传入xpath表达式来查找对应元素，并且只匹配第一个。//item表示标签名为item的标签
# item = r.xml.xpath('//item', first=True)
# print(item.text)

# 多个结果查询，利用循环对items这个迭代对象进行遍历，遍历出每一个查询到符合期望的标签名的对象。将对象内容添加到列表中。最后打印列表
items = r.xml.xpath('//link')
results = []
for i in items:
    results.append(i.text)
print(results)
for i in results:
    if 'https://www.nasa.gov' in i:
        break
else:
    assert False
