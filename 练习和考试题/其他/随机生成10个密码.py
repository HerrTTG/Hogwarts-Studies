lsa=list()
for i in range(26):
    lsa.append(chr(ord("a")+i))

for i in range(26):
    lsa.append(chr(ord("A")+i))


lsb=list()
for i in range(10):
    lsb.append(i)

#此案例的主要关键点在将list转换为集合，因为集合的无序特点。从集合中取出10个元素可以认为是随机的
d=set(lsa+lsb)

for i in range(10):
    print(d.pop(),end="")

'''
等价方式d=lsa+lsb

for i in range(10):
    print(random.choice(d),end="")'''