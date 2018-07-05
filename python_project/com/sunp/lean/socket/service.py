#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen()
while True:
    c,addr = s.accept()
    print("链接地址",addr)
    c.send('dddd'.encode())
    c.close()