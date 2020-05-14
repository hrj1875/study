'''class Student(object):
    #使用类名创建对象时，会自动调用初始化方法__init__()
    def __init__(self,name,age,adress,id,grade):
        self.name1=name
        self.age=age
        self.adress=adress
        self.id=id
        self.grade=grade
    def print_1(self):
        print('%s的年龄是%d,家庭住址在%s,学号是%d'%(self.name1,self.age,self.adress,self.id))
    def get_grade(self):
        if self.grade>=90:
            return 'A'
        elif 70<self.grade<90:
            return 'B'
        else:
            return 'C'
bart=Student('BOB bart',18,'beijing',1901,89)
print(bart.print_1())
print(bart.get_grade())
bart.name1='hello'
print(bart.name1)'''
'''class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_1(self):
        print('%s取得的%d'%(self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('error')
bart=Student('bart bob',91)
#bart.__name='hello'
bart.set_score('A')
print(bart.get_score())'''
'''class Animal(object):
    def __init__(self,name,type):
        self.name=name
        self.type=type
    def run(self):
        print('the animal  is running')
class Dog(Animal):
    def run(self):
        print('the dog is running')
class Cat(Animal):
     def run(self):
         print('the cat is running')
a=Animal('二哈','dog')
b=Cat('mao','big')
c=Dog('gou','big')
print(getattr(b,'name'))'''
# class Student(object):
#     count=0
#     def __init__(self,name):
#         self.name=name
#         Student.count=Student.count+1
# name1=Student('A')
# name2=Student('B')
# name3=Student('C')
# print(Student.count,Student.name)
'''class A:
    def test(self):
        print('test')
class B:
    def demo(self):
        print('demo')
class C(A,B):
    pass
#创建子类对象
c=C()
c.test()
c.demo()'''
'''class Dog(object):
    def __init__(self,name):
        self.name=name
    def game(self):
        print('%s play game'%self.name)
class XianTianDog(Dog):
    pass
class Person:
    def __init__(self,name):
        self.name=name
    def game_with_dog(self,dog):
        print('%s和%spaly game'%(self.name,dog.name))
wangcai=XianTianDog('旺财')
wangcai.game()
xiaoming=Person('小明')
xiaoming.game_with_dog(wangcai)'''
'''class Tools():
    count=0
    @classmethod
    def show_tool_count(cls):


        print('工具对象的数量%d'%cls.count)
    def __init__(self,name):
        self.name=name
        Tools.count+=1
tool1=Tools('dao')
tool2=Tools('qiang')
Tools.show_tool_count()'''
'''class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        #1.创建对象时，new方法会被自动调用
        print('创建对象，自动给分配空间')
        #2.new方法的作用是，为对象分配空间；返回对象的引用
        return super().__new__(cls)
    def __init__(self):
        print('播放器初始化')
music1=MusicPlayer()
print(music1)'''

