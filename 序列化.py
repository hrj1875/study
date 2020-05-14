import pickle
'''d=dict(name='bob',age=18,score=98)
str=pickle.dumps(d)
f=open('dump.txt','wb')
f.write(str)
f.close()'''
'''f=open('dump.txt','rb')
str=pickle.load(f)
print(str)
f.close()'''
'''import json
class Student:
    def __init__(self,name,age,score):
        self.name1=name
        self.age1=age
        self.score1=score
s=Student('Hilary','20','100')
def Studentdict(std):
    return{'name':std.name1,
           'age':std.age1,
           'score':std.score1}
print(json.dumps(s,default=lambda obj:obj.__dict__))
def Studendict2(d):
    return Student(d['name'],['age'],['score'])'''
#json_str='{"name":"Bob","age":20,"score":100}'
#print(json.loads(json_str,object_hook=Studendict2))
import json
obj=dict(name='小明',age='20')
str=json.dumps(obj,ensure_ascii=True)
print(str)