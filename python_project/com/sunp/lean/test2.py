'''
Created on 2018年6月25日

@author: tonglian
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    1 / 0
except Exception as e:
    '''异常的父类，可以捕获所有的异常'''
    print ("0不能被除")
else:
    '''保护不抛出异常的代码'''
    print("没有异常")
finally:
    print ("最后总是要执行我")

    
a = [{"a","b","c"},{1,2,3,4}]
for k in  a:
    print("%s" %(k ))
    
str = r"c:\a.text"
print(str)
str2 = "c:\\a.text"
print(str2)

str3 = "\r"
print(str3,"\\r")
str4 = "\n"
print(str4,"\\n")


class Test:
    def prt(self):
        print(self)
        print(self.__class__)
        
t = Test()
t.prt()
