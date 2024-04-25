import socket

# 创建socket对象
import turtle

server = socket.socket()
# 绑定端口
server.bind(('127.0.0.1', 9999))
# 监听端口
server.listen(1)
# 等待链接
conn, address = server.accept()
print("客户端的地址是{}".format(address))

# 接收数据
data = conn.recv(1024)
print(data.decode('utf-8'))

msg = 'I am server,msg is {}'.format((data.decode('utf-8')))

# 发送数据
conn.send(msg.encode('utf-8'))

conn.close()

server.close()
