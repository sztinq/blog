import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sa = ('127.0.0.1',8024)
s.bind(sa)
s.listen(20)

while True:
    cinfo, caddr = s.accept()
    print "Got a connection from %s" %caddr[0]
    data = cinfo.recv(1024)
    print "Receive data: %s" %data
    cinfo.send("echo:" + data)
    cinfo.close()
