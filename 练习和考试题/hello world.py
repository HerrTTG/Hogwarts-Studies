msg = "Hello World"
d = int(input())
number = [0, 2, 4, 6, 8, 10]

if d == 0:
    print(msg)
elif d > 0:
    for i in number:
        print(msg[i : i + 2])
elif d < 0:
    for i in range(11):
        print(msg[i])
else:
    print()
