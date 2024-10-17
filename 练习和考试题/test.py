ls = [str(i) for i in range(3)]

a = set()
b = set(ls)

for i in ls:
    a.update(i)

print(a, b)
