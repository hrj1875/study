'''from multiprocessing import Process
import os
def run_proc1(name):
    print('run child process1 %s (%s)'%(name,os.getpid()))
    print('going to')
def run_proc2(name1):
    print('run child process2 %s (%s)'%(name1,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.'%os.getpid())
    p=Process(target=run_proc1,args=('test',))
    print('child process will strat')
    p.start()
    p.join()
    #（Process()函数 group:None,target表调用对象,就是子进程要执行的任务，
    # name为子进程的名字，args为传结target函数的位置参数，是一个元组，必须有逗号，如：args=('monico',)
    # kwargs为传结target函数的关键字参数，是一个字典，如：kwargs={'name':'monico','age':18})
    p1=Process(target=run_proc2,args=('test',)
    p1.start()
    p1.join()
    print('child process end')'''
'''from multiprocessing import Process,Pool
import os,time,random
def long_time_task(name):
    print('run task %s (%s)...'%(name,os.getpid()))
    start=time.time()
    time.sleep(3)
    end=time.time()
    inter=end-start
    return ('Task %s runs %0.2f seconds.' % (name, inter))
def main(name):
    a=long_time_task(name)
    print(a)

    #print('Task %s runs %0.2f seconds.' % (name, (end - start)))
if __name__=='__main__':
    print('Parent proccess %s'%os.getpid())
    p=Pool(6)
    for i in range(7):
        p.apply_async(main,args=(i,))
    print('waiting for all subprocess done')
    p.close()
    p.join()
    print('all process done')'''
'''import subprocess
print('$nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])
print('exit code:',r)'''
#进程之间的通信
#!/usr/bin/env python3
'''from multiprocessing import Process,Queue
import os,time
q=Queue()
def write(q1):
    print('process to write:%s'%os.getpid())
    for value in ['A','B','C']:
        print('put %s to queue'%value)
        q.put(value)
        time.sleep(3)
def read(q2):
    print('process to read:%s'%os.getpid())
    while True:
        value=q.get('abcd')
        print('get %s from queue'%value)
if __name__ == '__main__':
    pw=Process(target=write,args=('q',))
    pr=Process(target=read,args=('q',))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()'''
'''from multiprocessing import Process
import os
def show_info(title):
    print(title)
    print('module name:',__name__)
    print('parent process:',os.getpid())
    print('child process:',os.getpid())
def f(name):
    show_info('function f')
    print(name)
if __name__ == '__main__':
    show_info('main process line')
    p=Process(target=f,args=('children process',))
    p.start()
    p.join()
    print('process all done')'''

from multiprocessing import Process,Queue
q=Queue()
def p_put(*args):
    a=q.put(args)
    print('has put %s'%args)
def p_get(*args):
    print('%s wait to get...'%args)
    a=['A','b','c']
    print(q.get(a))
    print('%s get it'%args)
if __name__ == '__main__':
    pp=Process(target=p_put,args=('pp1',))
    pg=Process(target=p_get,args=('pg1',))
    pp.start()
    pp.join()
    pg.start()
'''class A:
    def __init__(self):
        self.n=2
    def add(self,m):
        print('self is {0} @A.add',format(self))
        self.n+=m
class B(A):
    def __init__(self):
        self.n=3
    def add(self,m):
        print('self is {0} @B.add',format(self))
        super().add(m)
        self.n+=3
b=B()
b.add(2)
print(b.n)'''
'''import threading,time
def loop():
    print('thread %s is running'%(threading.current_thread().name))
    n=0
    while n<6:
        n=n+1
        print('thread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s is end'%(threading.current_thread().name))
print('thread %s is running'%(threading.current_thread().name))
p=threading.Thread(target=loop,name='loopthread')
p.start()
p.join()
print('thread %s is end'%(threading.current_thread().name))'''
#LOCK
'''import threading,time
balance=0
lock=threading.Lock()
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
def run_thread(n):
    for i in range(100000):
        #lock.acquire()
        #try:
          change_it(n)
        #finally:
          #lock.release()
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t3=threading.Thread(target=run_thread,args=(8,))
#t4=threading.Thread(target=run_thread,args=(8,))
#t5=threading.Thread(target=run_thread,args=(8,))
#t6=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t3.start()
#t4.start()
#t5.start()
#t6.start()
t1.join()
t2.join()
t3.join()
#t4.join()
#t5.join()
#t6.join()
print(balance)'''
'''import threading
local_student=threading.local()
class Student():
    def __init__(self,name):
        self.name=name
def process_student():
    stu=local_student.student1
    print('hello %s in %s'%(stu,threading.current_thread().name))
def process_thread(name):
    local_student.student1=name
    process_student()
t1=threading.Thread(target=process_thread,args=('bob',),name='thread1')
t2=threading.Thread(target=process_thread,args=('alice',),name='thread2')
t1.start()
t2.start() '''