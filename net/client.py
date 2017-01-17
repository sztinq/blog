__author__ = 'tinq'
import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
saddr = ('127.0.0.1',8024)
c.connect(saddr)
c.send('Hello Server')
data = c.recv(1024)
print "Reply from server %s" %data