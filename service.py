#-*- coding = utf-8-*-
#@Time : 2020/6/27 10:59
#@Author :Ella
#@File :service.py
#@Software : PyCharm

import socket
'''
1、创建一个socket对象
socket()用于创建一个socket描述符，它唯一标识一个socket
socket(int domain,int type,int protocol)三个参数都有默认值
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

'''
2、将socket绑定到指定的地址，即指定能被外界访问的地址和端口
bind(int scokfd,const struct sockaddr *addr,socklen_t addrlen)
'''
sock.bind(("localhost", 8082))#localhost这个地址是自己的IP地址（例如：192.168.3.2）（ipv4地址，在命令行使用ipconfig命令查看），端口由自己决定


#3、监听，使用socket套接字的listen方法接受连接请求
sock.listen(1)  # 监听客户端连接
while True:
    '''
    4、服务器套接字通过socket的accept方法等待客户请求一个连接
    接受客户端的请求，返回值是一个新的socket描述符，它代表和客户端的新的连接，可以它它理解成是一个客户端的socket
    '''
    conn, addr = sock.accept()  # 接收一个客户端连接
    '''
    5、处理阶段服务器和客户端通过send和recv方法通信（传输数据）
    5、打印客户端的请求，recv()#无论客户还是服务器应用程序都用recv函数从TCP连接的另一端接受数据
    '''
    print(conn.recv(1024))  # 从接收缓冲读消息 recv buffer

    #6、响应客户端的请求，即向客户端发送请求
    conn.sendall(b"world")  # 将响应发送到发送缓冲 send buffer

    #7、传输结束，关闭连接...
    conn.close()
    break

