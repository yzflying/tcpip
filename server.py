import socket
import threading

sf = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建socket，ip和tcp协议为ipv4和tcp
sf.bind(('10.1.2.40', 8081))    #绑定服务器的IP和端口
sf.listen(5)        #设置监听,等待连接

def run(sk):
    while True:
        data = sk.recv(1024)                       #sk.recv表示：服务端接收来自sk客户端
        print('client say:' + data.decode('utf-8'))
        data1 = input('what do you want to send to client:')
        sk.send(data1.encode('utf-8'))       #sk.send表示：服务端发送给sk客户端


while True:   #循环搜索潜在的客户端，并创建进程，开启进程
    sk_soc, sk_add = sf.accept()  # 建立连接，sk_soc, sk_add分别为客户端的ip
    t = threading.Thread(target=run, args=(sk_soc, ))
    t.start()
    # print(threading.enumerate())
