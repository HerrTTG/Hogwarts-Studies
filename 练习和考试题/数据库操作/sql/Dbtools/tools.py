import csv
import os

files = "..\\datas\\"
path = os.path.abspath(files)


def get_csvs() -> list[tuple]:
    if os.path.exists(path):
        csv_files = [(os.path.splitext(f)[0], os.path.abspath(os.path.join(path, f))) for f in os.listdir(path) if
                     f.endswith('.csv')]
    return csv_files


def export_data(csv_files) -> dict:
    insert_data = {}
    for file in csv_files:
        key, value = file
        with open(value, 'r', encoding="utf-8") as f:
            ls = list(csv.reader(f))
            for i in range(len(ls[1:])):
                ls[i + 1] = [str.strip().strip("'") for str in ls[i + 1]]
        insert_data[key] = ls[1:]
    return insert_data


insert_data = export_data(get_csvs())
tabale_infos = {"Student": """
                    CREATE TABLE IF NOT EXISTS Student (SId varchar(10),
                    Sname varchar(10),
                    Sage datetime,
                    Ssex varchar(10));
                    """,
                "Course": """CREATE TABLE IF NOT EXISTS Course (CId varchar(10),
              Cname nvarchar(10),
              TId varchar(10)); 
              """,
                "Teacher": """CREATE TABLE IF NOT EXISTS Teacher (TId varchar(10),
              Tname varchar(10)); 
              """,
                "SC": """CREATE TABLE IF NOT EXISTS SC(SId varchar (10),
              CId varchar(10),
              score decimal(18,1)); 
              """}
