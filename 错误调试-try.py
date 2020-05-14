'''try:
    print('try.........')
    r=10/0
    print('result:',r)
except NameError as e:
    print('except:',e)
except ValueError as  e:
    print(e)
finally:
    print('finally')
print('END')'''
'''while True:
    try:
        x=int(float(input('请输入数字')))
        print('输入的数字是：',x)
        break
    except :
        print('输入错误')'''

'''try:
    fh=open('testfile','r')
    fh.write('这是一个测试文件，用于测试处理异常')
except IOError:
    print('没有找到相应文件')
except NameError as e:
    print(e)
else:
    print('写入成功')
    fh.close()'''
'''def foo(s):
    x=int(s)
    #if x==0:
        #raise ValueError('输入错误')
    return 10/x
def main():
 try:
    a=foo(0)
    print(a)
 except ValueError as e:
    print(e)
    #raise
main()'''
'''def foo(s):
    n = int(s)
    assert n != 0
    return 10 / n

def main():
    foo('0')'''
'''import logging
logging.basicConfig(level=logging.WARNING)
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)'''

