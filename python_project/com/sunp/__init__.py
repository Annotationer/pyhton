import re
a = re.split('\W+', 'runoob, runoob, runoob.')
#['runoob', 'runoob', 'runoob', '']
print(a)

a = re.split('(\W+)', ' runoob, runoob, runoob.') 
#['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
print(a)
a = re.split('\W+', ' runoob, runoob, runoob.', 1) 
#['', 'runoob, runoob, runoob.']
print(a)
a = re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
#['hello world']
print(a)
