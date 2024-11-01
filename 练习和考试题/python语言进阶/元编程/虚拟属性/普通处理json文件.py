import json

with open("/练习和考试题/python语言进阶/元编程/osconfeed-sample.json") as p:
    feed = json.load(p)

print(sorted(feed["Schedule"].keys()))

# 获取演讲者的name
print(feed["Schedule"]['speakers'][-1]['name'])
