'''class Student(object):
    pass

s=Student()
s1=Student()
s2=Student()
from  types import MethodType
def set_name(self,name):
    self.name=name
s.set_name1=MethodType(set_name,s)
s.set_name1('mingzi')
print(s.name)
Student.set_name2=MethodType(set_name,Student)
s1.set_name2('12')
s2.set_name2('13')
print(s1.name,s2.name)'''
'''class Student(object):
    __slots__ = ('name','age')
class Graduate(Student):
    __slots__ = ('id')
stu1=Graduate()
stu1.name='nihao'
print(stu1.name)'''
'''class Student(object):
    # def __init__(self,name):
    #     self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
         self.__name=name
s=Student()
s.name='nihao'
print(s.name)'''
'''class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,width):
        self.__width=width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        self.__height=height
    @property
    def resolution(self):
        return self.height*self.width
s=Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')'''
'''class  Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
    __repr__=__init__
stu=Student('bob')
stu'''
'''class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10:
            raise StopIteration()
        return self.a

# for i in Fib():
#     print(i)
f=Fib()
print(f[1])'''
'''class Fib(object):
    def __getitem__(self, item):
        if isinstance(item,int):
          a,b=0,1
          for i in range(item):
            a,b=b,a+b
          return a
        elif isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                start=0
                a,b=1,1
                l=[]
                for i in range(stop):
                    a,b=b,a+b
                    l.append(a)
                return l
            else:
                a, b = 1, 1
                l = []
                for i in range(stop):
                  a, b = b, a + b
                  l.append(a)
                return l
f1=Fib()
print(f1[:5])'''
'''class Student(object):
    def __setitem__(self, key, value):
        self.key=key
        self.value=value
    def __delitem__(self, key):
        self.key=key
stu=Student()
stu.__setitem__('math',99)
# stu.__setitem__('math',98)
# stu.__setitem__('chinese',99)
stu.__delitem__('math')
print(stu.key,stu.value)'''
'''from enum import Enum
mouth=Enum('month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec','Hhh'))
for name,member in mouth.__members__.items():
    print(name,'->',member,',',member.value)'''
from enum import  Enum,unique
@unique
class weekday(Enum):
    sun=0
    mon=1
    tue=2
    wes=3
    thr=4
    fir=5
    san=7
day1=weekday()
print(day1.member.value)








