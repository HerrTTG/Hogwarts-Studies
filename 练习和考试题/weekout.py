# weekout.py

x = int(input())
weekstr = "星期一星期二星期三星期四星期五星期六星期天"

print(weekstr[(x - 1) * 3 : (x - 1) * 3 + 3])
