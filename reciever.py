import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print("ENter your IP")
ip=input()
print("ENter your PORT")
port=int(input())
s.bind((ip,port))

while True:
  x=s.recvfrom(1024)
  clientIP=x[1][0]
  data=x[0].decode()
  print("{}:{}".format(clientIP,data))
  
 
