fo = open("D:\\Python\\练习和考试题\\文本处理\\写入1.csv", "w", encoding='utf-8')

ls=["北京",'101.5','120.7','121,4']

fo.write(",".join(ls)+"\n")
#将一个一维列表转为一行，join取出每一个元素，并且逗号隔开，最后在文本末尾增加换行符\n
fo.close()