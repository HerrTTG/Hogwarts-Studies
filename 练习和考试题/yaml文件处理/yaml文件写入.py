import yaml

# 要写入的数据
data = {
	"userid": "zhangsan",
	"name": "张三",
	"alias": "jackzhang",
	"mobile": "13800000000",
	"department": [1],
	"order": [10, 40],
	"position": "产品经理",
	"gender": "1",
	"email": "zhangsan@gzdev.com",
	"is_leader_in_dept": [1],
	"enable": 1,
	"telephone": "020-123456",
	"address": "广州市海珠区新港中路",
	"extattr": {
		"attrs": [{
			"type": 0,
			"name": "文本名称",
			"text": {
				"value": "文本"
			}
		},
			{
				"type": 1,
				"name": "网页名称",
				"web": {
					"url": "http://www.test.com",
					"title": "标题"
				}
			}
		]
	},
	"to_invite": True,
	"external_position": "高级产品经理",
	"external_profile": {
		"external_attr": [{
			"type": 0,
			"name": "文本名称",
			"text": {
				"value": "文本"
			}
		},
			{
				"type": 1,
				"name": "网页名称",
				"web": {
					"url": "http://www.test.com",
					"title": "标题"
				}
			},
			{
				"type": 2,
				"name": "测试app",
				"miniprogram": {
					"appid": "wx8bd8012614784fake",
					"pagepath": "/index",
					"title": "1231"
				}
			}
		]
	}
}


# 写入 YAML 文件
with open('output.yaml', 'w', encoding='utf-8') as file:
    yaml.safe_dump(data, file)
