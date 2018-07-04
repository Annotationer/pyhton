#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
'''
i = 1
while i < 3:
    print("aa")
    i = i + 1
    
    
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
      else:                  # 循环的 else 部分
        print (num, '是一个质数')
        
'''

'''
def change(a):
    a = 10
    return a


i = 1
i = change(i)
print(i)

def changeList(a):
    a[0]="1"
    
list = ["a","b","c"]
changeList(list)
print(list)

def printInfo():
    print("sdsdsd")
    
printInfo()

def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("Name: ", name);
   print ("Age ", age);
   return;
 
#调用printinfo函数
printinfo( 50, "miki" );
'''

'''
def printinfo( arg1, *vartuple ):
    print ("输出: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return;
 
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, [60, 50]);

"""
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:       
   print ('当前水果 :', fruit)
"""
import calendar

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal);

import time
a = "Sat Mar 28 22:24:24 2016"
print( time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
        
'''

Money = 2000
def AddMoney():
    global Money
    #Money = 0
    Money = Money + 1
    #print(Money)
   
print (Money)
AddMoney()
print(Money)
       
        
        
        
        
        