import socket

# 连接服务器
client = socket.socket()
client.connect(('127.0.0.1', 9999))
msg = "你好,世界"
client.send(msg.encode('utf-8'))

data = client.recv(1024)

print(data.decode('utf-8'))

client.close()
