def getinput():
    s=input()
    return s

def word(s):
    s_new=""
    for i in s:
        if ord(i)>=ord("a") and ord(i)<=ord("z"):
            s_new+=i
        elif ord(i)>=ord("A") and ord(i)<=ord("Z"):
            s_new+=i
        else:
            continue
    return s_new

def main():
    s=getinput()
    print("{}".format(word(s)))


main()