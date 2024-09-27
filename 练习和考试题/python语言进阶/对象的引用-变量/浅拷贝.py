l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1)
print(l1 == l2, l1 is l2)
# 目前相同值，但不是同一个

l1.append(100)
print(l1, l2)
print(l1 == l2, l1 is l2)
# l1追加100 l2并不会发生变化，因为l2和l1最外层容器的ID不同 即[]不是同一个，即使里面的内容是相同的。但并不是同一个list。


l1[1].remove(55)
print(l1, l2)

print(l1[0] is l2[0])
print(l1[1] is l2[1])
print(l1[2] is l2[2])

l2[1] += [33, 32]
print(l1, l2)
print(l1[1] is l2[1])

l2[2] += (10, 11)
print(l1, l2)
print(l1[2] is l2[2])
