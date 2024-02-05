import yaml

# 读取 YAML 文件, 以前面复杂结果数据为例
with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)

# 处理读取到的数据
print(data)
print(data['cool_list'])
print(data['hard_list'][2]['test'])
