'''
Created on 2018年6月25日

@author: tonglian
'''

'''
fo = open ("a.txt","r+")

str = fo.read(10)
print(str)
position = fo.tell()
print("当前位置",position)
print("当前位置  %d " %position)
fo.seek(0,2)
#str = fo.read(-5)
#print(str)
fo.close()
import os
os.rename("a.txt","b.txt")
'''
'''
str2 = fo.readline()
print(str2)
fo.seek(0,0)
str3 = fo.readline()
print(str3)
'''

'''
def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)

functionName(0)
'''

'''
try:
    functionName(0)
except Exception:
    print("异常")
  '''

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
  
try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print (e.args)  
    

  
  