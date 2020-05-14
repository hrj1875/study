import os
'''str=os.environ.get()
print(str)'''
str=os.path.abspath('.')
print(str)
os.path.join('/Users/Hilary','test.txt')
#os.mkdir('/Users/Hilary/test.txt')
#os.rmdir('/Users/Hilary/test.txt')
str1=os.path.splitext('/Users/Hilary/test.txt')
print(str1)
a=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(a)
b=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.jpg']
print(b)