
def getnum():

    num =[]
    s=input("请输入一个数字:") 
    while s !=" ":
        try:
            num.append(eval(s))
            s=input("请输入一个数字:") 
            continue
        except:
            break
    return num
        

def calcm(n):
    sum=0
    for i in n:
        sum+=i
    return sum/len(n),sum

def fc(n,m):
    sdev=0.0
    for i in n:
        sdev=sdev+(i-m)**2
    
    return pow(sdev/len(n)-1,0.5)

def mid(n):
    n.sort(key=None)
    newn=n
    size=len(newn)
    if size % 2 ==0:
        med=(newn[size//2-1]+newn[size//2])/2
    else:
        med=newn[size//2]
    return med

def main():
    n=getnum()
    m,sum=calcm(n)
    print("输入的个数为:{},平均值为:{:.2f},方差:{:.2f},中位数:{:.2f},累计和:{}".format(len(n),m,fc(n,m),mid(n),sum))
    

main()