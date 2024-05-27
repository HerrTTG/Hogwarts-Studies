def right_to_left(message):
    """
    中间是你要实现的代码
    message is str
    """
    ls = message.split(' ')[::-1]
    _tmp = []
    for i in ls:
        if i != '':
            _tmp.append(i)

    return ' '.join(_tmp)


if __name__ == '__main__':
    print(right_to_left(" Thank you very    much.  "))
