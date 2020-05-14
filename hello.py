# #print('''line1
# #...line2
# #...line3''')'''
# '''
# #input函数
# '''
# a=input('请输入正方形的边长：')
# print('面积：%f'%(float(a)*float(a)))
#  #格式化
# a=input('请输入姓名：')
# print('hello,%s'%a)
# print('hello,{0},grade has went保留小数点后几位{1:.2f}%'.format('a',14.789))
#  #list
# classmates=[1,2,3,'f']
# classmates[1]='mary'
# classmates.append('kk')
# classmates.insert(0,'k')
# classmates.pop(1)
# print(classmates)
# if判断
# lengh=input('小明身高：')
# weight=input('小明体重：')
# bmi=float(weight)/(float(lengh)*float(lengh))
# if bmi<18.5:
#     print('小明过轻')
# elif 18.5<bmi<25:
#     print('正常')
# else:
#     print('肥胖')
#
# #for循环
# sum=0
# for x in range(0,100):
#     sum+=x
# print(sum)
# #while循环
# n=9
# while n<100:
#     if n>10:
#       break
#     print(n)
#     n=n+1
# #dict（key-value）
# grade={'a':98,'b':78,'c':90.5}
# grade['a']=99
# grade.pop('a')
# grade.get('a')
# print(grade)
# grade={'a':90,'b':98}
# d=2
# grade[d]='a little'
# print(grade)
# s1=set([1,2,3,4])
# s1.add(8)
# s1.remove(1)
# s2=set([4,3,8])
# s3=s1&s2
# print(s3)
# a='abc'
# b=a.replace('a','A')
#
# print(a)
# print(b)
# a=[7,3,6,8]
# a.sort()
# print(a)
# a=-378
# b=abs(a)
# print(b)
#
# n1=255
# n=hex(n1)
# print(n)
#
# def haha(x):
#     if x>9:
#         print(1)
#     else:
#         print(0)
# b=haha(1)
#
# import math
# def bb(x,y,step,angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y+step*math.sin(angle)
#     return nx,ny
# x,y=bb(89,27,100)
# print(x,y)
#
# import math
# def quadratic(a,b,c):
#   if a==0:
#       raise TypeError('a can not 0!')
#   else:
#       if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
#           raise TypeError('bad opreade type')
#       else
#           d=b*b-4*a*c
#           if d>0:
#            x1 = (-b + math.sqrt(d))/(2*a)
#            x2 = (-b - math.sqrt(d))/(2*a)
#            return (x1,x2)
#           else:
#               return ('无解')
# egg=quadratic(2,3,1)
# print(egg)
#
# def powr(x,n=2):
#     return x**n
# a=powr(5,3)
# print(a)
#
# def power(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# a=power(5,4)
# print(a)
# def add1(l=[]):
#   l.append('end')
#   return l
# a=add1()
# print(a)
# b=add1()
# print(b)
# def power(x):
#     return x
# a=power(3)
# print(a)
# b=power(4)*a
# print(b)
# def add1(l=[]):
#     if l is not None:
#         l=[]
#         l.append('end')
#         return l
# a=add1()
# print(a)
# b=add1()
# print(b)
#
# def cacl(*number):
#     sum=0
#     for n in number:
#         sum=sum+n*n
#     return sum
# a=cacl(*[2,3,4],2)
# #nums1=[1,2,3]
# #nums2=2
# #a=cacl(*nums1,nums2)
# print(a)
'''
def f1(x,y,**h):
    print('name:',x,'age:',y,'other:',h)
extra={'city':'beijing','gender':'女','classmate':'1930'}
a=f1('mary',18,**extra)
#递归函数
def fact(n):
    if n==1:
        return 1
    else:
        t=fact(n-1)*n
        return t
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
a=fact(1000)
print(a)
l=['bob','mary','lindar','han']
a=l[0:3]
# for i in range(0,2):
#     a=l[i]
print(a)
def trim(s):
   n=len(s)
   if s[0]==' ' and s[-1]==' ':
       return(s[1:n])
   elif s[0]==' ' and s[-1]!=' ':
       return(s[1:n])
   elif s[-1]==' ' and s[0]!=' ':
       return(s[0:n-1])
a=trim('hello ')
print(a)
l={'a':2,'b':3,'c':'hello'}'''
# for key in l.values():
#     print(key)
# for x, y in l.items():
#     print(x,y)
#判断是否可迭代
# from collections import  Iterable
# a=isinstance('aa',Iterable)
# print(a)
#标出下标

# for x,y in enumerate(l):
#     print(x,y)
# for x,y in ((1,2),(2,5)):
#     print(x,y)
          # 在list中找到最大值和最小值
# def findminandmax(l):
#      if not isinstance(l,list):
#          raise TypeError('')
#      if l!=[]:
#          min,max=l[0],l[0]
#          for x in l:
#              if not isinstance(x,(int,float)):
#                  raise TypeError('不是数不能比较大小')
#              if max<x:
#                  max1=x
#              elif min>x:
#                  min1=x
#          return (max1,min1)
# c=findminandmax([2,3,9,0])
# print(c)
#l=['Hello','World',18,'Apple','None']
# i=0
# while i<=4:
#     if isinstance(l[i],str):
#         a=l[i]
#         i=i+1
#         b=[a.lower()]
#     print(b)
# a=[x.lower() for x in l if isinstance(x,str)]
# print(a)
# def fb(max):
#     n,a,b=0,0,1
#     while n<max:
#         #print(b)
#         yield b
#         a,b=b,a+b
#         n=n+1
#     return 'done'
# c1=next(fb(3))
# c2=next(fb(3))
# c3=next(fb(3))
# print(c1,c2,c3)
# c4=next(fb(3))
# print(c4)
# c=fb(3)
# c5=next(c)
# print(c5)
# c6=next(c)
# print(c6)
# c=fb(6)
# for d in c :
#  print(d)
'''c=fb(6)
while True:
    try:
           d=next(c)
           print(d)
    except StopIteration as e:
            print('Generator return value:',e.value)
            break'''
'''def tragile(numraw):
    if numraw==0:
        return[]
    elif numraw==1:
        return[[1]]
    elif numraw==2:
        return[[1],[1,1]]
    n=3
    rlist=[[1],[1,1]]
    while n<numraw+1:
        newlist = [1]
        b=len(rlist[-1])
        c=b-1
        for i in range(c):
            newlist.append(rlist[-1][i]+rlist[-1][i+1])
        newlist.append(1)
        rlist.append(newlist)
        n=n+1
    return rlist
a=tragile(6)
print(a)'''
from functools import reduce
'''def a(s):
    digits={'0':0,'1':1,'2':2,'3':3,'5':5,'7':7,'9':9}
    return digits[s]
def fn(x,y):
    return x*10+y
b=reduce(fn,map(a,'13579'))
print(b)'''
'''l1 = ['adam', 'LISA', 'barT']
def normalize(name):
    a=name.lower()
    return a
a=map(normalize,l1)
print(list(a))'''
'''def pord(x,y):
    return x*y
a=reduce(pord,[3,5,7,9])
print(a)'''
'''def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    l1=list(map(int,s[:n]))
    l2=list(map(int,s[n+1:]))
    return reduce(fn,l1)+reduce(fn,l2)/10**len(l2)
print('\'123.456\'转化为浮点数:',str2float('123.456'))'''
'''def _odd():
    n=1
    while True:
        n=n+2
    yield n
def discon(n):
    return lambda x:x%n>0
def primes():
    yield 2
    it=_odd()
    while True:
        n=next(it)
        yield  n
        it= filter(discon(n),it)
    return it
    for n in primes():
       if n<10:
        print(n)
       else:
         break
a=primes()
print(list(a))'''
from operator import itemgetter
'''def byname(t):
     return t[1]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
b=sorted(L,key=byname)
print(b)'''
'''def is_palidom(n):
    return n==int(str(n)[::-1])
output=filter(is_palidom,range(1,200))
print(list(output))'''
'''def count():
    fs=[]
    for i in range(1,4):
        #def f():
        a=i*i
        fs.append(a)
    return fs'''
'''def count():
    fs=[]
    for i in range(1, 4):
     def f():
            return i*i
     fs.append(f())
    return fs
f1,f2,f3=count()
print(f1(),f2(),f3())'''
'''def creatcounter():
    i=[0]
    def counter():
        i[0]=i[0]+1
        return i[0]
    return counter
counterA = creatcounter()
print(counterA(), counterA())'''

'''def creatcounter():
    global i
    i=0
    def counter():
        global i
        i=i+1
        return i
    return counter
counterA = creatcounter()
print(counterA(), counterA())'''
'''def creatcounter():
    def counter():
        i=0
        while True:
          i=i+1
          yield i
    it=counter()
    def number():
        return next(it)
    return number
counterA = creatcounter()
counterB=creatcounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())'''
'''def count():
    fs=[]
    for i in range(1,4):
        def f():
            t=i*i
            fs.append(t)
            return fs
    return f
f1=count()
f2=count()
f3=count()
print(f1(),f1())
print(f2(),f3())
f4,f5=count()
a=f1()
if isinstance(a,list):
    print('ok')
    print(list(a))'''
'''def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1,f2,f3=count()
print(f1(),f1(),f3())'''
'''def foo():
    i=0
    while True:
        i=i+1
        yield i
print('hello')
a=foo()
print(next(a),next(a))'''
'''f=list(filter(lambda x:x%2==1,range(1,20)))
print(f)'''
'''def log(func):
    def wrapper(*h,**kw):
        print('%s',func.__name__)
        return func(*h,**kw)
    return wrapper
#@log
def now():
    print('2019-9-17')
b=log(now)
print(b())'''
#import functools
# a=functool3s.partial(max,9)
# print(a((1,2,3,10)))
# float1=functools.partial(pow,10)
# a=float1(2)
# print(a)
'''import functools
import time
import string
import random
li = [random.choice(string.ascii_letters) for i in range(100)]
def timer(func):
    functools.wraps(func)
    def wrapper(*h,**kw):
        starttime=time.time()
        func()
        endtime=time.time()
        print(endtime - starttime)
        return func()

    return wrapper
@timer
def odd():
    s=''
    for i in li :
        s=s+i+','
   # time.sleep(0.78)
    return s
a=odd()
print(a)'''
















