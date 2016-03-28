import socket
import sys

def send_file(filename):
    s = socket.socket()
    s.connect(("192.168.122.30",9999))
    f=open ("uploads/"+filename, "rb")
    l = f.read(1024)
    while (l):
        print l
        s.send(l)
        l = f.read(1024)
    f.close()
    s.close()
