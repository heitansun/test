import re
from datetime import time

'''
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
re.match(pattern=, string=, flags=)
'''

content = 'Hello 1234567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

# result = re.match('^Hello\s.*o$', content)
# print(result)
# print(result.group())
# print(result.group(3))

# print(result.group(1))


# line = "Cats are 1235 smarter than dog"
# html = "http://www.baidu.com"
# print(html)
# result1 = re.match('^c.*?5\s(\w+)\s(\w+)\s', line, re.I)
#
# result2 = re.match('^h.*?u\.', html, re.S)
# print(result1.group(2))
# print(result1.span())
# print(result2.group())
# r = result2.span()
# a = r[1]
# msg = '<html><h1>abc</h1></html>'
# result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
# print(result)
#
#
# msg = '<html><h1>abc</h1></html>'
# result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$',msg)
# print(result)


# def func(temp):
#     num = temp.group()
#     num1 = int(num)+5
#     return str(num1)
#
# result = re.sub(r'\d+',func,'java:99,python:95')
# print(result)
# result = re.split(',','java:99,python:95')
# print(result)

# from multiprocessing import Process
# import time
# import os
#
# m = 1
#
#
# def task(s, content):
#     global m
#     while True:
#         time.sleep(s)
#         m += 1
#         print(f'.....1{m}.........{content}', os.getpid(), '--------', os.getppid())
#
#
# def task2(s, content):
#     global m
#     while True:
#         time.sleep(s)
#         m += 1
#         print(f'-----2{m}---------{content}', os.getpid(), '*********', os.getppid())
#
#
# number = 1
# if __name__ == '__main__':
#     print(os.getpid())
#     # 子进程
#     p = Process(target=task, name='任务1', args=(1, 'aa'))
#     p.start()
#     print(p.name)
#     p1 = Process(target=task2, name='任务2', args=(2, 'bb'))
#     p1.start()
#     print(p1.name, os.getpid())
#
#     while True:
#         number += 1
#         time.sleep(0.5)
#         if number == 100:
#             p.terminate()
#             p1.terminate()
#             break
#         else:
#             print('------', number)
#
#     print('---------------')
#     print('***************')

#
# from multiprocessing import Process
#
#
# class MyProcess(Process):
#     def __init__(self, name):
#         super(MyProcess, self).__init__()
#         self.name = name
#
#     # 重写run方法
#     def run(self) -> None:
#         n = 1
#         while True:
#             print(f'{n}------>自定义进程，n：{self.name}')
#             n += 1
#
#
# if __name__ == '__main__':
#     p = MyProcess('小明')
#     p.start()
#
#     p1 = MyProcess('lily')
#     p1.start()

# from multiprocessing import Pool
# import time, os
# from random import random
#
# def task(task_name):
#     print(f'开始做任务！{task_name}')
#     start = time.time()
#     time.sleep(random() * 2)
#     end = time.time()
#     # print(f'{task_name}完成任务，用时：{end - start}，进程id：{os.getpid()}')
#     return f'{task_name}完成任务，用时：{end - start}，进程id：{os.getpid()}'
#
# container = []
#
# def callback_func(n):
#     print('test--->')
#     container.append(n)
#
# if __name__ == '__main__':
#     p = Pool(5)
#
#     tasks = ['听音乐', '看书', '写文章', '打游戏', '吃饭', '看电影', '写代码']
#     for taskName in tasks:
#         p.apply_async(task, args=(taskName,), callback=callback_func)
#
#     p.close()  # 添加任务结束
#     p.join()  # 堵住主进程
#     # 因为主进程结束后，所有的子进程会一起结束，所有当执行下面print('Over!!!')执行之后，相当于主进程
#     # 就结束了，所以添加join堵住进程结束，这样得以让上面的代码执行完才去下面的内容！
#
#     for c in container:
#         print(c)
#     print('Over!!!')

# import os, time
# from random import random
# from multiprocessing import Pool
#
#
# def task(taskName):
#     print(f'现在运行-->{taskName}的进程')
#     start = time.time()
#     time.sleep(random() * 2)
#     end = time.time()
#     print(f'{taskName}-->进程号：{os.getpid()}--->一共花费时间为：{end - start}')
#
#
# if __name__ == '__main__':
#     p = Pool(5)
#
#     tasks = ['听音乐', '看书', '写文章', '打游戏', '吃饭', '看电影', '写代码']
#     for name in tasks:
#         p.apply(task, args=(name,))
#
#     p.close()
#     p.join()


from multiprocessing import Queue

# q = Queue(5)
#
# q.put('1')
# q.put('2')
# q.put('3')
# q.put('4')
# q.put('5')
# print(q.qsize())  # 获取队列的长度
# if q.full():  # q.full() 判断队列是否满的;  q.empty() 判断队列是否是空的;
#     print('队列已满！')
# else:
#     q.put('f', timeout=3)  # put()  如果queue满了则只能等待，除非有‘空地’则添加成功
#
# print('Over')
#
# # 获取队列的值
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# print(q.get(timeout=2))
# if q.not_empty:
#     print('keep up')
# q.put_nowait(2)
# q.get_nowait()


# from multiprocessing import Process, Queue
# import time
#
#
# def download(q):
#     images = ['1.png', '2.png', '3.png', '4.png', '5.png']
#     for image in images:
#         print('Download...', image)
#         time.sleep(0.5)
#         q.put(image)
#
#
# def getfile(q):
#     while True:
#         try:
#             file = q.get(timeout=2)
#             print(f'{file}Save Successfully!')
#         except:
#             print('全部Save successfully！')
#             break
#
#
# if __name__ == '__main__':
#     q = Queue(2)
#     p1 = Process(target=download, args=(q,))
#     p2 = Process(target=getfile, args=(q,))
#
#     p1.start()
#     # p1.join()
#
#     p2.start()
#     p2.join()
#     print('所有数据都写完并且读完')

# import time
# from multiprocessing import Pool, Manager
#
#
# def download(q):
#     images = ['1.png', '2.png', '3.png', '4.png', '5.png']
#     for image in images:
#         print('Download...', image)
#         time.sleep(0.5)
#         q.put(image)
#
#
# def getfile(q):
#     while True:
#         try:
#             file = q.get(timeout=2)
#             print(f'{file}Save Successfully!')
#         except:
#             print('全部Save successfully！')
#             break
#
#
# if __name__ == '__main__':
#     q = Manager().Queue()
#     p = Pool(5)
#
#     p.apply(download, args=(q,))
#     p.apply(getfile, args=(q,))
#     p.close()
#
# import time
# import threading
#
#
# def download(n):
#     images = ['1.png', '2.png', '3.png', '4.png', '5.png']
#     for image in images:
#         print(f'{image}...is downloading！')
#         time.sleep(n)
#         print(f"{image} -->Download is successful!")
#
#
# def listenMusic(n):
#     misic = ['a', 'b', 'c', 'd', 'f']
#     for m in misic:
#         time.sleep(n)
#         print('正在听歌！', m)
#
#
# if __name__ == '__main__':
#     t = threading.Thread(target=download, name='aa', args=(1,))
#     t.start()
#
#     t1 = threading.Thread(target=listenMusic, name='bb', args=(1,))
#     t1.start()
#
#     n = 1
#     while True:
#         print(n)
#         time.sleep(1.5)
#         n += 1

# from threading import Thread
# import time
#
# money = 10000
#
#
# def run1():
#     global money
#     for i in range(5000):
#         # time.sleep(0.1)
#         money -= 1
#         # print(money, 't1')


# def run2():
#     global money
#     for i in range(5000):
#         # time.sleep(0.1)
#         money -= 1
#         # print(money, 't2')
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=run1, name='t1')
#     t2 = Thread(target=run2, name='t2')
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print('money:', money)


# from threading import Thread
# import time
#
# n = 0
#
#
# def task1():
#     global n
#     for i in range(1000000):
#         n += 1
#     print('--->task1：', n)
#
#
# def task2():
#     global n
#     for i in range(1000000):
#         n += 1
#     print('--->task2：', n)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=task1)
#     t2 = Thread(target=task2)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print('最后打印n：', n)


# import threading
# import random
# import time
#
# lock = threading.Lock()
#
# lis1 = [0] * 10
#
#
# def task1():
#     # 获取线程锁，如果已经上锁，则等待锁的释放
#     lock.acquire()  # 阻塞
#     for i in range(len(lis1)):
#         lis1[i] = 1
#         time.sleep(0.5)
#
#     lock.release()
#
#
# def task2():
#     # 获取线程锁，如果已经上锁，则等待锁的释放
#     lock.acquire()  # 阻塞
#     for i in range(len(lis1)):
#         print('------->', i)
#         time.sleep(0.5)
#
#     lock.release()
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task1)
#     t2 = threading.Thread(target=task2)
#
#     t1.start()
#     t2.start()
#
#     # t1.join()
#     # t2.join()

from threading import Lock, Thread
import time

lockA = Lock()
lockB = Lock()


class MyThread(Thread):
    def run(self) -> None:
        if lockA.acquire():  # 如果可以获取到锁则返回iTrue
            print(self.name + '获取了A锁')
            time.sleep(0.1)
            if lockB.acquire(timeout=5):  # 阻塞
                print(self.name + '又获取了B锁，原来还有A锁')
                lockB.release()
            lockA.release()


class MyThread1(Thread):
    def run(self) -> None:
        if lockB.acquire():  # 如果可以获取到锁则返回True
            print(self.name + '获取了B锁')
            time.sleep(0.1)
            if lockA.acquire(timeout=5):  # 阻塞
                print(self.name + '又获取了A锁，原来还有A锁')
                lockA.release()
            lockB.release()


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread1()

    t1.start()
    t2.start()
