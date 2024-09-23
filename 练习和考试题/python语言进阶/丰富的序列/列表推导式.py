# 列表推导式的妙用
# 其本身涵盖了map和filter两个函数的功能
ls = [str(i) for i in range(1, 1000) if i > 500]

# 如果用mapfilter来写就会非常复杂
# 要注意的是filter和map的souce都必须是一个可迭代对象。
# 所以要先生成一个la列表，在对la这个列表做filter过滤符合条件的结果。最后在map进行全部转换。
# 可见代码行数变多了不少，但可读性也并没有提升太多。
la = []
for i in range(1, 1000):
    la.append(i)
la = list(map(str, filter(lambda x: x > 500, la)))

print(ls)
print(la)
