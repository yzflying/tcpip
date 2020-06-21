import socket


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建socket，指定ip和tcp协议为ipv4和tcp
sk.connect(('10.1.2.40', 8081))           #指定连接服务器的ip地址和端口号,建立连接

# sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')  #分段给服务器发送数据
# data = []
while True:              #每次循环接收1024字节数据
    data = input('what do you want to send to server:')
    sk.send(data.encode('utf-8'))
    info = sk.recv(1024)
    print('server say:', info.decode('utf-8'))


