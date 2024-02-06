# 从1到966

s = 0

for i in range(1, 966 + 1):
    if i % 2 != 0:
        # 偶数除2的余数位0，故判断不为0的为奇数
        s = s + i
    else:
        s = s - i
print(s)
