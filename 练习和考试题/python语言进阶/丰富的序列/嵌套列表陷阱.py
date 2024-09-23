ls = [['_'] * 3] * 3
print(ls)
ls[0][0] = 'a'
print(ls)

row = ['_'] * 3
la = []
for i in range(3):
    la.append(row)

lt = [['_'] * 3 for i in range(3)]
lt[0][0] = 'a'
print(lt)

lo = []
for i in range(3):
    lo.append(['_'] * 3)

lo[0][0] = 'a'
print(lo)
