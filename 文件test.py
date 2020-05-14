'''fh=open('photo.jpg','rb')
a=fh.read()
print(a)'''
'''fh=open('test.txt','w',encoding='gbk')
fh.write('这是测试')
fh.close()
fh1=open('test.txt','r+')
str1=fh1.read()
print(str1)
fh1.close()
fh2=open('test.txt','r+')
str2=fh2.read()
print(str2)
fh2.close()
fh4=open('test.txt','a+',encoding='gbk')
fh4.write('这是测试追加')
fh4.close()
fh5=open('text.txt','r+')
print('文件名：',fh5.name)
str5=fh5.read()
print(str5)
fh5.close()'''

'''fh=open('test1.txt','w+',encoding='gbk')
print('文件名：',fh.name)
print('权限：',fh.mode)
print('文件是否关闭：',fh.closed)
fh.write('重头测试')
str=fh.read()
print(str)
fh.close()
fh1=open('test1.txt','r')
str1=fh1.read()
print(str1)'''
import  os
'''fh=open('test2.txt','a+',encoding='gbk')
fh.write('123abc+中国')
f=fh.tell()
print(f)
fh.seek(f,0)
str=fh.read()
print(str)
fh.close()
fh=open('test2.txt','r')
print(fh.read())
fh.close()'''
'''with open('test.txt','r') as f:
    print(f.readlines(1))
    print(f.readlines(3))
    print(f.read(6))
    print(f.readlines())
    print(f.readlines())
    f.close()'''
'''import os
filepath=os.listdir('C:/Users/Hilary/PycharmProjects/untitled')
with open('test2.txt','r') as f:
 print(f.read(2))
print(filepath)'''
'''with open('test.txt','r')as f:
    postion=f.seek(2,0)
    str=f.read(6)
    print(str)
    f.close()'''



