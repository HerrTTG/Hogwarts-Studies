# 一周7天5天进步2天退步

day = 1.0
dayq = 0.01

for i in range(365):
    if (i + 1) % 7 in [0, 6]:
        day = day * (1 - dayq)
    else:
        day = day * (1 + dayq)
print("{:.2f}".format(day))
