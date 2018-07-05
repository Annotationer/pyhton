#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018年7月4日

@author: tonglian
'''
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))
print(s.recv(1024))
s.close()
