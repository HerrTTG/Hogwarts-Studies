from datetime import timedelta


class Child_Sheet():
    __range = "D3:F13"

    def __init__(self, wb, billcycle):
        # 检查 billcycle 是否是合法的标识符
        if not billcycle.isidentifier():
            raise ValueError(f"'{billcycle}' is not a valid identifier.")

        self.__wb = wb[billcycle]

        # 使用 eval 来动态设置属性
        try:
            self.__dict__[billcycle] = Child(self.__wb[self.__range])
        except Exception as e:
            raise ValueError(f"Error evaluating: {e}")

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value


class Child():
    def __init__(self, sheet):
        for row in sheet:
            row_name = row[0].coordinate + row[1].coordinate + row[2].coordinate
            self.__dict__[row_name] = self.__calc(row)

    def __calc(self, row):
        start, end, usetime = row
        if start.value is not None and usetime.value is not None and end.value is None:
            if isinstance(usetime.value, str):
                return start.value, start.value + self.__split(usetime.value), usetime.value
        return start.value, end.value, usetime.value

    def __split(self, value):
        return timedelta(*tuple(map(int, value.split(":"))))

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield key, value


if __name__ == "__main__":
    import openpyxl

    test = (Child_Sheet(openpyxl.load_workbook(".//Bill Run Status_child.xlsx"), "BC01"))
    print(test.BC01.D3E3F3)
