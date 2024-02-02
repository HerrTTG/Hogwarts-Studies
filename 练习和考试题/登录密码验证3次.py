for i in range(3):
    username = input()
    password = input()
    if username == "Kate" and password == "666666":
        print("登录成功！")
        break
else:
    print("3次用户名或者密码均有误！退出程序。")
