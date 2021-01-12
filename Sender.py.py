#!/usr/bin/env python
# coding: utf-8

# In[2]:


import socket


# In[3]:


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


# In[4]:


print("Enter Your IP")
ip=input()
print("Enter Your port")
port=int(input())
print("Enter Your Partner")
pip=input()
print("Enter Your Partner port")
pport=int(input())


# In[5]:


s.bind((ip,port))


# In[ ]:


while True:
    print("enter message")
    msg=input().encode()
    s.sendto(msg,(pip,pport))
    


# In[ ]:




