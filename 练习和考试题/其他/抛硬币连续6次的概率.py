import random

num=0
lt = []
for expectnumer in range(10000):
    ls = []
    for i in range(100):
        ls.append(random.randint(0, 1))
    random.shuffle(ls)
    for i in range(0,100,6):
        if i <95:
            if ls[i:i+6]==[0,0,0,0,0,0] or ls[i:i+6]==[1,1,1,1,1,1]:
                num+=1
                for t in range(6):
                    lt.append(ls[i:i+6])
            else:
                continue

print("{:.2f}%".format((num/10000)*100))
