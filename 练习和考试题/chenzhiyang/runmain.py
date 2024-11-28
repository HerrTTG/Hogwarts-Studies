import openpyxl
from typing import Generator

from My_sheet import Child_Sheet


def load(wb) -> Generator:
    sheet_name = ["BC01", "BC02", "BC03", "BC04", "BC06", "BC07", "BC08"]
    for bc in sheet_name:
        yield Child_Sheet(wb, bc)


def write_to_summry(sumrry_path, chilid_path):
    # if sumrry_path is None or os.path.exists(sumrry_path) is False :
    #     sumrry_path=generate_summry_file()

    output_wb = openpyxl.load_workbook(sumrry_path)
    input_wb = openpyxl.load_workbook(chilid_path)
    child_wb = load(input_wb)

    writer = _write()
    for i in range(8):
        writer(output_wb["12"], child_wb)
    else:
        output_wb.save(sumrry_path)


# def generate_summry_file():
#     pass

def _write():
    start_row = 3
    columns = ['D', 'E', 'F']

    def inner(wb, child):
        nonlocal start_row
        try:
            for row, value in next(child):
                if "BC" in row:
                    child_sheet = value
                # print(vars(child_sheet))
            for row, value in child_sheet:
                for index, colum in enumerate(columns):
                    wb[f'{colum}{start_row}'] = value[index]
                else:
                    start_row += 1
            else:
                start_row += 4
        except StopIteration:
            pass

    return inner


if __name__ == "__main__":
    write_to_summry(sumrry_path=".//Bill Run Status_Summary.xlsx", chilid_path=".//Bill Run Status_child.xlsx")
