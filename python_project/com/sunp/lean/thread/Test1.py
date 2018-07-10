#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _thread
import time

#为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" %(threadName,time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time,("thread-1", 2))
    _thread.start_new_thread(print_time,("thread-2", 4))
except Exception as err:
    print(err.args)
    print("Error")

'''
finally:
    _thread.exit_thread()
'''

    
while True:
    pass