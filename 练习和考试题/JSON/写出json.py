pythonvalue={'iscat':True,'miceCaught':0,'name':'Zophie'}
#json不能储存每一种python的值，它只能包含以下数据类型值：字符串，整型，浮点型，布尔型，列表、字典和Nonetype。

import json
strofJsondata=json.dumps(pythonvalue)

print(strofJsondata)