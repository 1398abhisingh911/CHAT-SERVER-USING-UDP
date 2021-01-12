def recieve():
    while True:
      x=s.recvfrom(1024)
      clientIP=x[1][0]
      data=x[0].decode()
      print("{}:{}".format(clientIP,data))
def send():
    while True:
      print("enter message")
      msg=input().encode()
      s.sendto(msg,(pip,pport))
    
    
import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("ENter your IP")
ip=input()
print("ENter your PORT")
port=int(input())

print("ENter your paratner IP")
pip=input()
print("ENter your partner PORT")
pport=int(input())


s.bind((ip,port))

x1=threading.Thread(target=recieve)
x2=threading.Thread(target=send)

x1.start()
x2.start()
