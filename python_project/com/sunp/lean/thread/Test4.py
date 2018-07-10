#-*- coding = UTF-8 -*-
'''
死锁问题实例
'''
import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        print("开启线程：" + self.name)
        #获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name,3)
        sub(self.name, 2)
        #释放锁，开启下一个进程
        threadLock.release()

def print_time(threadName, delay):
    time.sleep(delay)
    global counter
    counter -= 1
    print("%s: 减少  %d" %(threadName, counter))
    
    
def sub(threadName,delay):
    time.sleep(delay)
    global counter
    counter += 1
    print("%s: 增加  %d" %(threadName, counter))
    

threadLock = threading.Lock()
threads = []
counter = 10

thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("退出主进程")
    
        