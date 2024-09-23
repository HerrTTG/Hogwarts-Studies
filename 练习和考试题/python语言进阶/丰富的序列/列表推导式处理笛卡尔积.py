a = ('a', 'b', 'c')
b = (1, 2, 3)

c = [i * j for i in a for j in b]
print(c)

d = []
for i in a:
    for j in b:
        d.append(i * j)
print(d)
