# 3.10加入

# 基础用法
def fun(message):
    match message:
        case ['case1', a, b]:
            return a + b
        case ['case2', "test"]:
            return message[1]
        case _:
            raise ValueError(message)


# match 关键字后面的表达式是匹配对象，即各个case子句中尝试匹配的数据

# match还支持解构，这是一种高级拆包形式。
DATA = [('Tokyo', 'JP', (35, 139), "123", "abc"), ('Mexico City', 'MX', (19, -99), "321", "cba")]


def main():
    print(f'{"":15}|{"latitude":>9}|{"longitude":>9}')
    for record in DATA:
        match record:
            # case 后是解构模式和过滤条件
            case [name, _, (lat, lon) as coord, *other] if lon > 0:
                print(f'{name:15}|{coord[0]:9}|{coord[1]:9}')
                print(f'{"remark:":15}|{str(other):>19}')
            # 匹配逻辑如下：
            #             1.匹配对象是序列
            #             2.匹配对象模式中的项数和match的对象record项数相同
            #             3.对应的项互相匹配，包括嵌套的项
            #


if __name__ == "__main__":
    main()
