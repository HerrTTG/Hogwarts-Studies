#获取文件中只出现一次,即不重复的函数。


f = open("D:\\Python\\练习和考试题\\文本处理\\latex.log","r")
ls = f.readlines()
s = set(ls)
#s中是全部的行唯一值，但是包含重复的行
for i in s:
    ls.remove(i)
    #从ls中移除不重复的内容，即删除一次后就消失的内容。
t = set(ls)
#ls中剩下的是至少出现2次以上的内容，转变为不重复集合t。
print("共{}独特行".format(len(s)-len(t)))
#用全部的行S减去剩余的t，就是只出现一次的行数