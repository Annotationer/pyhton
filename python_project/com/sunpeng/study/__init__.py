'''
from test.test_builtin import Squares
name={'name':{'first':'Bob','last':'Smith'},'job':['mgr','dev'],'age':40}
print(name)
print(name['job'])
ks=list(name['job'])
print(ks)
ks.sort()
print(ks)
ks2 = list(name.keys())
print(ks2)

for key in name:
    print(key,"=>",name[key])
    
print("_____________")
for key in sorted(name):
    print(key,"=>",name[key])
    
print("---------------")
print(name)
for c in name:
    print(name[c])

squares=[]
for x in [1,2,3,4,5]:
    squares.append(x**2)
print(squares)

if not 'f' in name['name']:
    print('missing')

value=name.get('name', 0)
print(value)

val=name['name'] if 'a' in name else 0
print(val)

if 'a' in name :
    print(name[name])
else:
    print('1')
'''
from _overlapped import NULL
from math import floor
from test.test_functools import decimal

"""
T=(1,2,3,4)
print(T)
T + (5,6)
print(T + (5,))
"""

'''
f=open('data.txt','w')
f.write('Hello\n')
f.write('world\n')
f.close()

w=open('data.txt')
text =w.read()
print(text)
print(text.split())

print(dir(w))

data=open('data.bin','rb').read()
print(data)
'''


'''
x=set('spam')
y={'h','a','m'}
print(x)
print(x-y)
'''


'''
print(1.0/3.0)

import decimal
d=decimal.Decimal('3.14')
print(d+1)
#Decimal('4.41')

from fractions import  Fraction
f=Fraction(2,3)
print(f+1)

decimal.getcontext().prec=2
val =decimal.Decimal('1.00')/decimal.Decimal('3.00')
print(val)
print(1>2)
'''
'''
print(bool('spam'))
x=None
print(x)

L={1,2,3}
type(L)
'''

'''
class Worker:
    def __init__(self,name,pay):
        self.name=name
        self.pay=pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *=(1.0 + percent)
        
        
bob=Worker('Bob Smith',50000)
sue=Worker('Sue Jones',60000)
print(bob.lastName())
print(sue.lastName())
sue.giveRaise(0.1)
print(sue.pay)


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
a=Student("AAA",20)
print(a.name)

'''

'''
import abc
class File(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def click(self):
        pass

class Text(File):
    def click(self):
        print('open file')
text=Text()
text.click()


a=1+1j
b=2j
print(a*b)
print(a.real)
print(a.imag)


print(hex(12))
print(oct(12))
print(bin(12))

print(5>>2)

print(a!=b)
print(1/2)
'''

'''
L=list(range(1000))
print(L[10:1001:100])
print(L)
b=L[slice(10,1001,100)]
print(b)

a=2**3
print(a)
'''

'''
b=1/3
print(b)
print(repr(b))
print(str(b))


import math
math.floor(1)


print(-5/2)
print(-5//2)


print(2**100)

'''

'''
import random

print(random.choice(['A','B','C']))


print(0.1+0.1+0.1-0.3)
'''


'''
import decimal
decimal.getcontext().prec=4
pay=decimal.Decimal(str(1999+1.33))
print(pay)
print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))
with decimal.localcontext() as ctx:
    ctx.prec =2
    print(decimal.Decimal('1.00')/decimal.Decimal('3.00'))

from fractions import  Fraction
print(Fraction('0.25')+Fraction('1.25'))
print(Fraction(1,10)+Fraction(1,10)+Fraction(1,10)-Fraction(3,10))
print((2.5).as_integer_ratio())
f=2.5
print(Fraction(*f.as_integer_ratio()))
print(float(1/3))

print(Fraction.from_float(1.75))

print(*(1.75).as_integer_ratio())


print(*(1/2).as_integer_ratio())

'''
x = set('abcde')
y = set('bdxyz')
print(x)

z = x.intersection(y)
print(z)
#z.update(set(['xxx']))
z.update(set(['zzz','11']))
print(z)
for item in z :print(item)
a = set(['hello','world'])
print(a)

b= set(('AAA','bbb'))
print(b)

print(a>b)
print(a<b)
c= set(['AAA'])
print(c)
print(b>c)
print(b<c)
s=set()
s.add('AAA')
print(s)




