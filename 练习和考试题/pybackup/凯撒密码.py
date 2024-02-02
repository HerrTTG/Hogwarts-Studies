# 字符串运算
s = input()
t = ""
for c in s:
    if "a" <= c <= "z":
        t += chr(ord("a") + ((ord(c) - ord("a")) + 3) % 26)
        # 根据unicode编码得出的计算公式
    elif "A" <= c <= "Z":
        t += chr(ord("A") + ((ord(c) - ord("A")) + 3) % 26)
    else:
        t += c
print(t)
