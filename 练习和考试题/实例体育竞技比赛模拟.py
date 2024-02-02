#MatchAnalysis.py
from random import random
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")

def getInputs():
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次: "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    #AB的获胜场次
    for i in range(n):
        #比赛N场分解为判断比分的每一场，引入一个新的函数去判断单一场次结果
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    #单一场次模拟
    scoreA, scoreB = 0, 0
    serving = "A"
    #默认A先发球
    #写一个无限循环并判断结束的条件，将条件分装为一个函数，方便修改
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            #随机数判断A是否赢下此局，赢则A加1分，且发球不变。否则发球变为B
            if random() < probA:
                scoreA += 1
            else:
                serving="B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving="A"
    return scoreA, scoreB

def gameOver(a,b):
    #分装的比赛结束规则，当A或者B的分数等于15时，返回true
    return a==15 or b==15

def printSummary(winsA, winsB):
    #计算并输出比赛结果
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))

def main():
    #总框架分为四部分
    #输出介绍
    #输入用户参数
    #计算模拟
    #输出结果
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
main()

