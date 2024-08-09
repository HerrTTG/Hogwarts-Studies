import csv
import openpyxl

"""
需求：
将excel表格中的两个表（sheet1 sheet2）转为CSV文件，并修改其表头
将CSV文件导入表中，利用sql对其进行汇总。
输出sql查询结果，导入新的excel表格中。
"""


def replace_elements(header_colum, type):
    if type == 'A':
        # 原始的表头
        original_list = [
            '沟通时间', '填写人（自动）', '分配老师', '填写时间（自动）', '用户类型（自动）',
            '姓名（必填）', '手机号（必填）', '所在班级', '您这周想要跟老师沟通哪方面的问题？',
            '您这周想要跟老师沟通的具体问题是什么？', '请上传你的简历', '你本周意向沟通的老师是', 'AFK'
        ]

        # 替换后的表头
        replacement_list = [
            'Expect_time', 'User', 'Teacher', 'Create_time', 'User_type',
            'Name', 'Phone', 'Class', 'Title', 'Details',
            'File', 'Expect_teacher', 'AFK'
        ]
    else:
        # 原始的表头
        original_list = [
            '沟通时间', '填写人（自动）', '填写时间（自动）', '用户类型（自动）', '私教老师2',
            '请对今天讲师的授课进行打分（满分10分）（必填）', '请对今天班主任的表现进行打分（满分10分）（必填）',
            '对于本次授课内容是否满意（必填）', '请问你觉得哪里可以进行优化', '课程深浅度（必填）',
            '你对本次课程的吸收情况是？（必填）', '你认为有待改进的地方是'
        ]

        # 替换后的表头
        replacement_list = [
            'Communication_time', 'User', 'Create_time', 'User_type', 'Teacher',
            'Score_Teacher', 'Score_Teacher_director', 'Satisfaction_level', 'Suggestions',
            'Depth_degree', 'Acceptance_level', 'Improvement_points'
        ]

    # 创建替换规则字典
    # zip对两个列表中的元素进行匹配，匹配的生成一对元组 dict转为键值对
    replacement_dict = dict(zip(original_list, replacement_list))

    # 字典get方法获取item值，如果没有值则返回item
    # '沟通时间': 'Expect_time'
    # item ='沟通时间' 时 返回 'Expect_time'，作为新列表的元素
    # item ='其他未定义的列本身的表头索引'时 返回 '其他未定义的列本身的表头索引'
    return [replacement_dict.get(item, item) for item in header_colum]


def excel_to_csv(input_file, output_file, type):
    # 打开Excel文件
    workbook = openpyxl.load_workbook(input_file)
    sheet = workbook.active

    # 获取第一行作为表头
    header = [cell.value for cell in sheet[1]]

    # 找出所有表头不为空的列的索引
    valid_columns = [index for index, value in enumerate(header) if value is not None]

    # 如果没有有效的列，直接返回空文件
    if not valid_columns:
        open(output_file, 'w').close()
        return

    # 读取数据并保留有效列
    data = []
    for row in sheet.iter_rows(values_only=True):
        filtered_row = [row[index] for index in valid_columns]
        data.append(filtered_row)

    # 将data中的第一行，即header进行元素替换
    data[0] = replace_elements(data[0], type)

    # 将数据写入CSV文件
    with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)


if __name__ == '__main__':
    input_file = input("请输入被转换的excel文件地址(如C:\\Users\\96436\\Desktop\\A表.xlsx):")
    output_file = input("请输出csv存放地址(如C:\\Users\\96436\\Desktop\\A.csv):")
    type = input("请输入文件转换的表类型（A or B）")
    excel_to_csv(input_file, output_file, type)
