import socket
import threading

from stdatabase import ManagementDB


# 小扩展，尝试修改服务器能够和一个客户端多次重复的交互。

class MultiTaskTCPServer(object):
    # 在初始化方法中对服务端socket进行初始化操作
    def __init__(self, ip="", port=8080):
        # 创建tcp服务端套接字
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置端口号复用，让程序退出端口号立即释放
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定IP和端口号
        self.server.bind((ip, port))
        # 设置监听, listen后的套接字是被动套接字，只负责接收客户端的连接请求
        # 最大等待连接数设置为128
        self.server.listen(128)

    # 启动服务器方法，实现多任务接受处理客户端连接请求
    def run(self):
        print('服务器启动成功')
        # 循环等待接收客户端的连接请求
        while True:
            # 等待到客户端的连接请求后获取client和ipport
            # server.accept() 就是监听接收到客户端的请求连接，返回客户端的socket对象和addr
            client_socket, ip_port = self.server.accept()
            print("客户端连接成功:", ip_port)

            # 当客户端和服务端建立连接成功以后，创建一个处理客户端请求的子线程，
            # 不同子线程负责接收和处理不同客户端的请求
            # 多线程目标handle_client_request这个函数
            # 传参，客户段请求的client和ipport
            sub_thread = threading.Thread(target=self.handle_client_request,
                                          args=(client_socket, ip_port))

            # 设置守护主线程 一旦服务器被已关闭，那么无论子线程执行到何处都会被杀死
            # 使服务器下线就断开所有在运行的处理线程
            sub_thread.setDaemon = True

            # 启动子线程
            sub_thread.start()

            # self.server.close()
            # tcp服务端套接字可以不需要关闭，因为服务端程序需要一直运行
            # 直到服务器关闭方法被执行


    # 处理客户端的请求操作
    def handle_client_request(self, client, ip_port):
        # 接收客户端发送的数据并解码
        # 4096是读取字节一次性读多少字节
        # 原始数据是二进制的，需要decode才能变成字符串
        recv_data = client.recv(4096).decode("utf-8")
        # 如果接收的数据长度为0，说明客户端主动断开了连接
        if len(recv_data) == 0:
            print("客户端下线了:", ip_port)
            return

        # 解析客户端请求数据
        request = self.parserRequest(recv_data)

        # 创建连接学生管理系统数据库的对象
        self.st_db = ManagementDB(user='root', pwd='Kuoka314+',
                                  host='localhost', port=3306, database='hogwarts')

        # 路由分发接口
        # 根据不同的请求来寻找对应的函数进行操作，这个处理函数被称之为服务器的接口，找接口的方法叫做路由方法
        response = self.router(request)

        # 返回结果
        client.send(response)

        # 删除数据库连接对象
        del self.st_db

        # 终止和客户端进行通信
        client.close()

    # 解析请求报文的方法
    def parserRequest(self, recv_data):
        # GET /change?wd=123123&name=443 HTTP/1.1

        # 用来保存数据的字典
        request = {
            "method": "",
            "path": "",
            "values": {}
        }
        # 解析字符串默认空格分隔
        recv_data = recv_data.split()

        # 保存请求方式
        request["method"] = recv_data[0]

        # 再次分隔路径和参数
        path = recv_data[1]

        if '?' in path:
            # 出现问好说明有路径和参数需要进行分割
            _tmp = path.split('?')
            path = _tmp[0]
            # 提取参数
            params = _tmp[1].split("&")
            for s in params:
                # 分解查询参数字符串
                k, v = s.split("=")
                request["values"][k] = v

        request["path"] = path
        return request

    # 解析path的路由方法，用于分发接口
    def router(self, request):
        # print(request)
        response_body = ''.encode('utf-8')
        path = request.get("path")
        # 分发接口
        if path == '/add':
            response_body = self.stsadd(request.get('values'))
        elif path == '/change':
            response_body = self.stchange(request.get('values'))
        elif path == '/query':
            response_body = self.stquery(request.get('values'))
        elif path == '/del':
            response_body = self.stdel(request.get('values'))
        else:
            response_body = self.stindex()

        # 拼接接口返回的数据为报文体
        #消息头
        response = '''HTTP/1.1 200 OK\r\nContent-Type: text/html;charset=utf-8\r\nServer: MyWebServe V1.0\r\n'''
        response += '\r\n'
        response = response.encode('utf-8')

        #接口返回数据拼接
        response += response_body
        return response

    # 接口函数
    # 接口的返回都是统一二进制
    def stindex(self):
        # /index
        # 默认首页
        with open('./index.html', 'rb') as f:
            return f.read()

    def stsadd(self, values):
        # 新增数据接口
        # /add?sid=s09&name=lucy&age=23&gender=male
        return self.st_db.st_add(values)

    def stchange(self, values):
        # 修改接口
        # /change?sid=01&name=kevin&age=23&gender=male
        return self.st_db.st_change(values)

    def stquery(self, values):
        # 查询接口
        # /query?sid=s09
        return self.st_db.st_query(values)

    def stdel(self, values):
        # 删除接口
        ##/del?sid=01
        return self.st_db.st_del(values)



if __name__ == '__main__':
    # 创建服务器对象
    # ip='10.88.50.174'
    server = MultiTaskTCPServer(port=8080)
    # 启动服务器
    server.run()
