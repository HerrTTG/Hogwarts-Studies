from collections import OrderedDict

import matplotlib.pyplot as plt
import openpyxl
import os
import pandas as pd
from pandas import DataFrame
from pandas.core.groupby.generic import DataFrameGroupBy
from typing import AnyStr


# 将 Total Collection File Size 转换为数值（统一单位为 MB）
def convert_to_mb(value: AnyStr) -> float:
    if "GB" in value:
        return float(value.replace(" GB", "")) * 1024
    elif "KB" in value:
        return float(value.replace(" KB", "")) / 1024
    else:
        return float(value.replace(" MB", ""))


# xlsx中的str转数值，不然无法按照大小排序
def convert_str_tonumber(value: AnyStr) -> int | float:
    if isinstance(value, str):
        return int(value)
    return value


def draw(grouped: DataFrameGroupBy, xlsx_file_name: str) -> None:
    """
    每个文件都要绘制一共三张图File Number, File Size (MB), CDR Count
    """
    for metric in ["File Number", "File Size (MB)", "CDR Count"]:
        plt.figure(figsize=(10, 6))  # 创建一个新的图表，设置图表大小为10x6英寸

        for groupname, df in grouped:  # 按 Collection NE 分组，循环遍历每个组
            # name为NE名，data为其对应的每一行数据DF格式
            # 绘制xy，点为圆形，标签label为name
            plt.plot(df["End Date"], df[metric], marker="o", label=groupname)  # 绘制每组的折线图
        else:
            plt.title(f"{metric} Over Time", fontsize=14)  # 设置图表标题
            plt.xlabel("End Date", fontsize=12)  # 设置横轴标签
            plt.ylabel(metric, fontsize=12)  # 设置纵轴标签（当前指标）
            plt.legend(title="NE", fontsize=10)  # 添加图例，图例标题为NE
            plt.grid(True)  # 启用网格线，方便查看数值
            plt.xticks(rotation=45)  # 将横轴标签旋转45度，避免重叠
            plt.tight_layout()  # 自动调整布局，避免文字重叠
            # plt.show()  # 显示图表
            # 保存折线图为 PNG 文件
            savepath = xlsx_file_name.replace(".xlsx", "") + f"_{metric}.png"  # 文件保存路径
            plt.savefig(savepath, format="png", dpi=300)  # dpi=300 保证高分辨率


def excel_to_dict(sheet) -> OrderedDict:
    """
    将表格转为映射类型，列头key，每一行数据组成的list为value
    """
    data = OrderedDict()

    #统一化表头
    for colum in sheet[1]:
        #Upload NE or Collection NE to NE
        if "NE" in colum.value:
            colum = "NE"
        #Upload File Number or Collection File Number to File Number
        elif "File Number" in colum.value:
            colum = "File Number"
        #Upload File Size or Collection File Size to File Size
        elif "File Size" in colum.value:
            colum = "File Size"
        else:
            colum = colum.value
        data[colum] = list()

    # 从第二行开始依次导入数据到对应的列的列表中
    row = 2
    # 判断此行中第一个元素值是否为空
    while sheet[row][0].value:
        keys = (colum for colum in data.keys())
        for cell in sheet[row]:
            data[next(keys)].append(cell.value)
        row += 1
    return data


def reindex(df: DataFrame) -> DataFrame:
    """
    索引重建，先分组。原因是不同组之间可能有重复的索引值，
    如NE1有12月1 NE2也会有12月1
    所以要分开处理。
    对每组的DF先生成最大最小时间的一个标准索引数据all_dates
    在设置End Date为索引
    reindex索引，依据为all_dates。缺失索引的行会被填充，并赋值Nah
    将Nah填充为0
    最后将索引index重新恢复列名End Date
    """
    new_dataframes = []
    grouped = df.groupby("NE")

    for groupname, df in grouped:
        # 用于生成一组连续的日期时间索引
        all_dates = pd.date_range(start=df["End Date"].min(), end=df["End Date"].max(), freq="D")

        # 将日期设为索引，利用 Pandas 的 reindex 方法补全缺失的日期，释放索引
        data = df.set_index("End Date").reindex(all_dates).reset_index()
        # 将Nah的数据填充为0 否则绘图会跳过
        data = data.fillna(0)

        # `reindex` 后的列名 "index" 恢复为 "End Date"
        data = data.rename(columns={"index": "End Date"})

        # 添加分组的 "NE" 列（因为自动补全的日期的行，是没有没有分组信息的）
        data["NE"] = groupname

        # 将补全后的 DataFrame 添加到新列表中，等待返回
        new_dataframes.append(data)

    # 合并所有补全后的分组数据，返回一个DF
    return pd.concat(new_dataframes, ignore_index=True)


def main(xlsx_files: list):
    for xlsx in xlsx_files:
        wb = openpyxl.load_workbook(xlsx)
        data = excel_to_dict(wb['sheet1'])

        # 创建 DataFrame
        df = pd.DataFrame(data)

        # 数据类型转换
        df["File Size (MB)"] = df["File Size"].apply(convert_to_mb)
        df["File Number"] = df["File Number"].apply(convert_str_tonumber)
        df["CDR Count"] = df["CDR Count"].apply(convert_str_tonumber)
        df["End Date"] = pd.to_datetime(df["End Date"])

        # 根据 NE 分组
        grouped = reindex(df).groupby("NE")

        # 绘制三张图
        draw(grouped, xlsx)


if __name__ == "__main__":
    input_path = input("xlsx`s path(Default to script running path):")
    if input_path == "":
        input_path = os.getcwd()

    xlsx_files = [file for file in os.listdir(input_path) if file.endswith(".xlsx") and not file.startswith("~")]
    main(xlsx_files)
