t = [1, 3, 4, 2, 5, 0]
t1 = [1, 3, 4, 2, 5, 0]
print(t.sort())  # 返回为none
print(t)  # 原始列表发生改变
print(sorted(t1))
print(t1)  # 原列表并没有发生改变
