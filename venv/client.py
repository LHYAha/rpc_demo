#-*- coding = utf-8-*-
#@Time : 2020/6/27 11:38
#@Author :Ella
#@File :client.py
#@Software : PyCharm
import socket

#1、创建socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#2、请求连接服务器
sock.connect(('192.168.7.41',8082)) #服务器端提供的IP地址和端口

#3、向服务器发送数据
sock.sendall(b"hello")

#4、接受并打印出服务器响应回来的内容
print(sock.recv(1024))

#5、关闭连接
sock.close()