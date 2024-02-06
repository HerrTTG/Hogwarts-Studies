




def checkmap(d,ls):
    w=0
    b=0
    wcheck={}
    bcheck={}

    for key in d.keys():
        if key not in ls:
            return  False
            break
        elif d[key][0]=='w':
            w=w+1
            if w>16:
                return False
                break
            elif d[key]=='wking':
                wcheck[d[key]]=wcheck.get(d[key],0)+1
                if wcheck[d[key]]>1:
                    return False
                    break
            elif d[key] =='wawn' :
                wcheck[d[key]]=wcheck.get(d[key],0)+1
                if wcheck[d[key]]>8:
                    return False
                    break
            elif d[key] =='wqueen' :
                wcheck[d[key]]=wcheck.get(d[key],0)+1
                if wcheck[d[key]]>1:
                    return False
                    break
            elif d[key] =='wbishop' :
                wcheck[d[key]]=wcheck.get(d[key],0)+1
                if wcheck[d[key]]>2:
                    return False
                    break
            elif d[key] =='wknight' :
                wcheck[d[key]]=wcheck.get(d[key],0)+1
                if wcheck[d[key]]>2:
                    return False
                    break
            elif d[key] =='wrook' :
                wcheck[d[key]]=wcheck.get(d[key],0)+1
                if wcheck[d[key]]>2:
                    return False
                    break

        elif d[key][0]=='b':
                b=b+1
                if b>16:
                    return False
                    break
                elif d[key] == 'bking':
                    bcheck[d[key]] = bcheck.get(d[key], 0) + 1
                    if bcheck[d[key]] > 1:
                        return False
                        break
                elif d[key] == 'bawn':
                    bcheck[d[key]] = bcheck.get(d[key], 0) + 1
                    if bcheck[d[key]] > 8:
                        return False
                        break
                elif d[key] == 'bqueen':
                    bcheck[d[key]] = bcheck.get(d[key], 0) + 1
                    if bcheck[d[key]] > 1:
                        return False
                        break
                elif d[key] == 'bbishop':
                    bcheck[d[key]] = bcheck.get(d[key], 0) + 1
                    if bcheck[d[key]] > 2:
                        return False
                        break
                elif d[key] == 'bknight':
                    bcheck[d[key]] = bcheck.get(d[key], 0) + 1
                    if bcheck[d[key]] > 2:
                        return False
                        break
                elif d[key] == 'brook':
                    bcheck[d[key]] = bcheck.get(d[key], 0) + 1
                    if bcheck[d[key]] > 2:
                        return False
                        break
        else:
            return True
            continue
    else:
        return True

def printmap(up_map):
    pls=[]
    for i in [8,7,6,5,4,3,2,1]:
        tls = []
        for a in range(8):
            tls.append(chr(ord('a')+a)+str(i)+':'+up_map[chr(ord('a')+a)+str(i)])
        pls.append(tls)

    for line in pls:
        for i in range(len(line)):
            print("{0:<10}".format(line[i]),end='|')
        print('\n',end='')
        for i in range(8):
            print("-"*10+'|',end='')
        print('\n')


#游戏开始的初始map
inital_map={'a8':'brook','b8':'bknight','c8':'bbishop','d8':'bking','e8':'bqueen','f8':'bbishop','g8':'bknight','h8':'brook',\
            'a7': 'bawn', 'b7': 'bawn', 'c7': 'bawn', 'd7': 'bawn', 'e7': 'bawn', 'f7': 'bawn', 'g7': 'bawn', 'h7': 'bawn',\
            'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ',\
            'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ',\
            'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ',\
            'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ',\
            'a2': 'wawn', 'b2': 'wawn', 'c2': 'wawn', 'd2': 'wawn', 'e2': 'wawn', 'f2': 'wawn', 'g2': 'wawn', 'h2': 'wawn',\
            'a1':'wrook','b1':'wknight','c1':'wbishop','d1':'wqueen','e1':'wking','f1':'wbishop','g1':'wknight','h1':'wrook'}


ls=[]
for i in [8,7,6,5,4,3,2,1]:
    for ch in ['a','b','c','d','e','f','g','h']:
        ls.append(ch+str(i))
        #棋盘行列

if checkmap(inital_map,ls) is True:
    printmap(inital_map)