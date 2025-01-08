from collections import OrderedDict

import csv

f = open("C:\\Users\\96436\\Desktop\\result.csv", 'r')
fr = csv.reader(f)
ls = []
for row in fr:
    ls.append([word for word in row[0].split(" ") if word != ""])


def csv_to_dict(ls):
    """
    将表格转为映射类型，列头key，每一行数据组成的list为value
    """
    data = OrderedDict()

    # 统一化表头
    for colum in ls[0]:
        data[colum] = list()

    # 从第二行开始依次导入数据到对应的列的列表中
    row = 1
    # 判断此行中第一个元素值是否为空
    while ls[row][0]:
        keys = (colum for colum in data.keys())
        for cell in ls[row]:
            data[next(keys)].append(cell)
        row += 1
    return data


csv_to_dict(ls)
