import requests

xml = """<?xml version='1.0' encoding='utf-8'?>
<a>6</a>"""

# request 没有封装专门的xml参数，所以要用到data来传递
# 并且必须在header中的contenttype写明是xml类型

header = {'Content-Type': 'application/xml'}

r = requests.post("https://httpbin.ceshiren.com/post",
                  data=xml, headers=header, verify=False)

print(r.text)
