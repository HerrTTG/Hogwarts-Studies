# 拆包对象可以进行嵌套如(a,b,(c,d))

DATA = [('Tokyo', 'JP', (35, 139), "123", "abc"), ('Mexico City', 'MX', (19, -99), "321", "cba")]


def main():
    print(f'{"":15}|{"latitude":>9}|{"longitude":>9}')
    for name, _, (lat, lon), *other in DATA:
        print(f'{name:15}|{lat:9}|{lon:9}')
        print(f'{"remark:":15}|{str(other):>19}')


if __name__ == "__main__":
    main()
