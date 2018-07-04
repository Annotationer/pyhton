#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

line = "Cats are smarter than dogs"

#matchObj = re.match(r'(.*) are (.*?) .*', line ,re.RegexFlag.M|re.RegexFlag.I)
matchObj = re.match(r'(.*) are (.*?) .*', line ,re.M|re.I)

if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    print ("matchObj.group(1) : ", matchObj.group(1))
    print ("matchObj.group(2) : ", matchObj.group(2))
else:
    print ("No match!!")

    
phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*', "", phone,2)
print ("电话号码是: ", num)
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone)
print ("电话号码是 : ", num)

num = re.sub(pattern = r"\D", repl = "",string = phone)
print(num)

# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
 
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
print(re.sub('(?P<value>\d+)', "", s))


pattern = re.compile(r'\d+') 
m = pattern.match('one12twothree34four') 
print(m)
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')
m.group(0)                            # 返回匹配成功的整个子串
#'Hello World'
m.span(0)                             # 返回匹配成功的整个子串的索引
#(0, 11)
m.group(1)                            # 返回第一个分组匹配成功的子串
#'Hello'
m.span(1)                             # 返回第一个分组匹配成功的子串的索引
#(0, 5)
m.group(2)                            # 返回第二个分组匹配成功的子串
#'World'
m.span(2)                             # 返回第二个分组匹配成功的子串
#(6, 11)
m.groups()                            # 等价于 (m.group(1), m.group(2), ...)
#('Hello', 'World')
'''m.group(3) '''                           # 不存在第三个分组    
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#IndexError: no such group

pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
 
print(result1)
print(result2)
    