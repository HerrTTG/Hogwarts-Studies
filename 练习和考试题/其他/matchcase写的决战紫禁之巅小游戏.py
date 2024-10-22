def uerinput() -> list[tuple[str, str]]:
    p1 = input("西门吹雪出招是为:")
    p2 = input("叶孤城出招是为:")
    return [('西门吹雪', p1), ('叶孤城', p2)]


def check(turn: list[tuple[str, str]]) -> bool:
    match turn:
        case [('西门吹雪', p1), ('叶孤城', p2)] if p1 != '' and p2 != '':
            print(f'西门吹雪使出了{p1}！')
            print(f'叶孤城使出了{p2}！')
            winer = (p1, p2)

            print('经过了激烈的交锋....')
            match winer:
                case ('三尺七寸的利剑' as x, y) if y != '天外飞仙':
                    print(f'西门吹雪的绝招{x}险胜叶孤城的{y}')
                    return False
                case (x, '天外飞仙' as y) if x != '三尺七寸的利剑':
                    print(f'叶孤城的绝招{y}险胜西门吹雪的{x}')
                    return False
                case ('三尺七寸的利剑' as x, '天外飞仙' as y):
                    print(f'两人均使出了自己的绝招{x}和{y},剑锋交错，不分胜负！')
                    return True
                case _:
                    print('未能分出胜负')
                    return True

        case [('西门吹雪', p1), ('叶孤城', p2)] if p1 == '':
            print(f'西门吹雪没有出招！叶孤城胜利！')
            return False
        case [('西门吹雪', p1), ('叶孤城', p2)] if p2 == '':
            print(f'叶孤城没有出招！西门吹雪胜利！')
            return False
        case _:
            return False


def pk():
    count = 1
    while True:
        print(f"第{count}回合决斗!开始！")
        if check(uerinput()):
            count += 1
        else:
            print(f'双方共交手{count}回合')
            break


if __name__ == '__main__':
    pk()
