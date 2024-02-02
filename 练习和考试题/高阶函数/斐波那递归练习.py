def fei(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fei(n - 1) + fei(n - 2)


def main():
    i = int(input())
    print(fei(i))


main()
