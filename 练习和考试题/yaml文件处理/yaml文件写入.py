import yaml

# 要写入的数据
data = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': {
        'key4': 'value4'
    }
}

# 写入 YAML 文件
with open('output.yaml', 'w') as file:
    yaml.safe_dump(data, file)
