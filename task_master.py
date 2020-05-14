#分布式进程
import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
task_queue=queue.Queue()
result_queue=queue.Queue()
class Queuemanager(BaseManager):
    pass
def return_task_queue():
    global task_queue # 定义成全局变量
    return task_queue # 返回发送任务的队列
def return_result_queue():
    global result_queue
    return result_queue # 返回接收结果的队列
def test():

    #序列化不支持匿名函数
    #是一个类方法，可以将一个类型或者可调用对象注册到管理器类。,阻塞状态由于等待某个事件发生而无法执行，便放弃处理机而处于阻塞状态，引起的原因有等待I/O完成，申请缓冲区不能满足。
    Queuemanager.register('get_task_queue1',callable=return_task_queue)
    Queuemanager.register('get_result_queue',callable=return_result_queue)
    manager=Queuemanager(address=('127.0.0.1',8001),authkey=b'abc')
    manager.start()
    task=manager.get_task_queue1()
    result=manager.get_result_queue()
    for i in range(10):
        n=random.randint(0,1000)
        print('Put task %d...'%n)
        task.put(n)
    print('Try get results...')
    for i in range(10):
        r=result.get()
        print('Result:%s'%r)
    manager.shutdown()
    print('master exit')
if __name__ == '__main__':
    freeze_support()
    print('START')
    test()