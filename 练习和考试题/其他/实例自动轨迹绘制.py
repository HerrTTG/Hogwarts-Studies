import turtle as t 



def getinterface():

    interface=open("D:\\Python\\自动绘图脚本.txt",'r')
    ls=list()
    for line in interface:
        line = line.replace("\n", "")
        #print(line)
        ls.append(list(map(eval, line.split(","))))
        #一维数据转二维数据，将一行字符串，变成一个列表，按照字符串中的逗号作为分割每一个元素。在将这个列表，变为二维列表中的一个元素。
    #print(ls)
    interface.close()
    return ls



def draw(ls):
    for i in range(len(ls)):
        t.pencolor(ls[i][3],ls[i][4],ls[i][5])
        t.fd(ls[i][0])
        if ls[i][1]==0:
            t.left(ls[i][2])
        else:
            t.right(ls[i][2])




def main():
    t.title("自动轨迹绘制")
    t.setup(800, 600, 0, 0)
    t.pencolor("red")
    t.pensize(5)
    draw(getinterface())
    t.done()

main()