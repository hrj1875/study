'''小明体重是70kg,
小明每一次跑步会减肥0.5gongjin
小明每一次吃东西体重会增加1公斤'''
class Person(object):
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return '%s的体重是 %.2f'%(self.name,self.weight)
    def run(self):
        self.weight-=0.5
        return self.weight
    def eat(self):
         self.weight+=1
         #return self.weight
xiaoming=Person('小明',70.50)
xiaoming.run()
xiaoming.run()
xiaoming.eat()
print(xiaoming)