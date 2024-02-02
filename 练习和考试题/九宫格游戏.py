import  random
import sys
import time

d=dict()
for i in range(9):
    d.setdefault(i,str(i))

def printBoard(d):
    print(d[0] + '|' + d[1] + '|' + d[2])
    print('-----')
    print(d[3] + '|' + d[4] + '|' + d[5])
    print('-----')
    print(d[6] + '|' + d[7] + '|' + d[8])

def gameover(d):
    if d[2] == d[4] == d[6]:
        return True
    elif d[0] == d[4] == d[8]:
        return True
    else:
        for i in range(0,8,3):
            if d[i]==d[i+1]==d[i+2]:
                return True
                break
        for i in range(0,3):
            if d[i]==d[i+3]==d[i+6]:
                return True
                break
turn=random.randint(0,1)
if turn==0:
    turn='X'
else:
    turn='&'
sum=0
while sum<9:
    printBoard(d)
    print("Turn for " + turn + '. Move on which space?')
    try:
        move=int(input())
        if 0<=move<=8:
            d[move] = turn
            if gameover(d):
                print(turn + ' Win!')
                printBoard(d)
                sum=9
                break
        else:
            print('input wrong,please input 0~8')
            time.sleep(2)
            continue
    except:
        print('input wrong,please input 0~8')
        time.sleep(2)
    else:
        if turn =='X':
            turn='&'
        else:
            turn='X'
        sum+=1




