from collections import OrderedDict

import matplotlib.pyplot as plt
import openpyxl
import os
import pandas as pd


# 将 Total Collection File Size 转换为数值（统一单位为 MB）
def convert_to_mb(size):
    if "GB" in size:
        return float(size.replace(" GB", "")) * 1024
    elif "KB" in size:
        return float(size.replace(" KB", "")) / 1024
    else:
        return float(size.replace(" MB", ""))


def convert_str_tonumber(size):
    if isinstance(size, str):
        return int(size)
    return size


def draw(grouped, xlsx_file_name):
    for metric in ["File Number", "File Size (MB)", "CDR Count"]:
        # figsize=(10, 6)
        plt.figure()  # 创建一个新的图表，设置图表大小为10x6英寸
        for name, data in grouped:  # 按 Collection NE 分组，循环遍历每个组
            # name为group的列名，data为其对应的每一行数据
            # 绘制x坐标为每一行数据的enddate,y坐标为三张折线图的规定列数据，标签label为name
            plt.plot(data["End Date"], data[metric], marker="o", label=name)  # 绘制每组的折线图
        else:
            plt.title(f"{metric} Over Time", fontsize=14)  # 设置图表标题
            plt.xlabel("End Date", fontsize=12)  # 设置横轴标签
            plt.ylabel(metric, fontsize=12)  # 设置纵轴标签（当前指标）
            plt.legend(title="Collection NE", fontsize=10)  # 添加图例，图例标题为 Collection NE
            plt.grid(True)  # 启用网格线，方便查看数值
            plt.xticks(rotation=45)  # 将横轴标签旋转45度，避免重叠
            plt.tight_layout()  # 自动调整布局，避免文字重叠
            # plt.show()  # 显示图表
            # # 保存折线图为 PNG 文件
            savepath = xlsx_file_name.replace(".xlsx", "") + f"_{metric}.png"  # 文件保存路径
            plt.savefig(savepath, format="png", dpi=300)  # dpi=300 保证高分辨率


def update_dict(target_dict: OrderedDict):
    for colum in target_dict.keys():
        yield colum


def excel_to_dict(sheet):
    data = OrderedDict()
    # 转为映射类型，列头key，每一行数据组成的list为value
    for colum in sheet[1]:
        if "NE" in colum.value:
            colum = "NE"
        elif "File Number" in colum.value:
            colum = "File Number"
        elif "File Size" in colum.value:
            colum = "File Size"
        else:
            colum = colum.value
        data[colum] = list()

    # 从第二行开始依次导入数据到对应的列的列表中
    i = 2
    # 判断此行中第一个元素值是否为空
    while sheet[i][0].value:
        keys = update_dict(data)
        for cell in sheet[i]:
            data[next(keys)].append(cell.value)
        i += 1
    return data


def main(xlsx_files):
    for xlsx in xlsx_files:
        wb = openpyxl.load_workbook(xlsx)
        data = excel_to_dict(wb['sheet1'])

        # 创建 DataFrame
        df = pd.DataFrame(data)

        # 数据类型转换
        df["File Size (MB)"] = df["File Size"].apply(convert_to_mb)
        df["File Number"] = df["File Number"].apply(convert_str_tonumber)
        df["CDR Count"] = df["CDR Count"].apply(convert_str_tonumber)

        # 根据 NE 分组
        grouped = df.groupby("NE")

        # 绘制三张图
        draw(grouped, xlsx)


if __name__ == "__main__":
    input_path = input("xlsx`s path(Default to script running path):")
    if input_path == "":
        input_path = os.getcwd()

    xlsx_files = [file for file in os.listdir(input_path) if file.endswith(".xlsx") and not file.startswith("~")]
    main(xlsx_files)
