# -*- coding:utf-8 -*-
# import os
#
# path = os.path.dirname('/root/test.txt')
# cur_path = os.path.dirname(__file__)
# print(cur_path)
# print(path)

# 将/root/2.jpg 复制到本地文件夹中，并且名字为原名；
# """
# 1.复制文件
# 2.存储文件
# """
# import os
#
# file = '/root/2.jpg'
# oldFileName = os.path.basename(file) # 返回文件名
# oldFIlePath = os.path.dirname(file)  # 返回文件路径
# oldFile = os.path.join(oldFIlePath, oldFileName) # 拼接 路径 + 文件名
#
# path = os.path.dirname(__file__)
# newName = os.path.join(path, oldFileName)
#
# with open('/root/2.jpg', 'rb') as stream:
#     contains = stream.read()
#
# with open(newName, 'wb') as wstream:
#     wstream.write(contains)

#
# """
# 1.创建文件夹
# 2.添加文件
# 3.打开文件并读取
# 4.将读取的文件写入另外一个文件夹中
# 5.原名保存
# """
#
# import os
#
# path1 = '/root/tmp/test1'
# path2 = '/root/tmp/test2'
# fileContains = 'hello world!'
#
#
# # 创建test文件，数量及内容可以自己调用进行添加
# def makefile(number, fileContains, path1, path2):
#     if os.path.exists(path1):
#         print(f'{path1}已存在，无须再创建！')
#     else:
#         os.makedirs(path1)
#         print(f'{path1}文件创建成功！')
#     if os.path.exists(path2):
#         print(f'{path2}已存在，无须再创建！')
#     else:
#         os.makedirs(path2)
#         print(f'{path2}文件创建成功！')
#     for i in range(0, number):
#         with open(f'{path1}/{i}.txt', 'a+') as wstream:
#             wstream.write(fileContains)
#     counts = os.listdir(path1)
#     print(f'共创建了{len(counts)}份文件！')
#
#
# # makefile(10, fileContains, path1, path2)
#
# def copy(path1, path2):
#     fileList = os.listdir(path1)
#     for file in fileList:
#         fileName1 = os.path.join(path1, file)
#         fileName2 = os.path.join(path2, file)
#
#         if os.path.exists(fileName2):
#             print(f'{file}文件已存在！')
#
#         elif os.path.isdir(fileName1):
#             os.mkdir(fileName2)
#             copy(fileName1, fileName2)
#
#         else:
#             with open(fileName1, 'rb') as stream:
#                 r = stream.read()
#
#             with open(fileName2, 'wb') as wstream:
#                 wstream.write(r)
#             print(f'{file}复制成功！')
#
#
# copy(path1, path2)

# import os
#
#
# def calculate():
#     try:
#         n1 = int(input('输入数字：'))
#         print(n1)
#         # return 1
#
#     except ValueError:
#         print('输入的数字错误')
#         # return 2
#
#     else:
#         print('数字输入完毕！')  # 没有异常才会执行的代码块
#
# calculate()

# def func():
#     stream = None
#     try:
#         stream = open('/root/11timg.jpeg', 'rb')
#         container = stream.read()
#         print(container)
#         return 1
#
#     except Exception as err:
#         print(err)
#         return 2
#
#     finally:
#         print('-------finally-----------')
#         if stream:
#             stream.close()
#             print('---表示执行了该代码块------')
#         return 3
#
# result = func()
# print(result)

# def register():
#     username = input('请输入用户名：')
#     if len(username) < 6:
#         raise Exception('用户长度必须6位以上！')
#     else:
#         print('输入的用户名是：', username)
#
# try:
#     register()
# except Exception as err:
#     print(err)
#     print('注册失败！')
#
# else:
#     print('注册成功！')

# names = ['tom', 'lily', 'lucy', 'lilei', 'jack', 'steven', 'bob', 'kally']
#
#
# result = [name.title() for name in names if len(name) > 5]
# print(result)

# def func(names):
#     list1 = []
#     for name in names:
#         if len(name) > 2:
#             list1.append(name.title())
#     return list1
#
#
# result = func(names)
# print(result)

# result = [n for n in range(0, 102) if n % 3 == 0 and n % 5 == 0]
# print(result)

# def func():
#     list1 = []
#     for i in range(5):
#         if i % 2 == 0:
#             for j in range(5):
#                 if j % 2 != 0:
#                     list1.append((i, j))
#     return list1
#
#
# result = func()
# print(result)
#
# result = [(i, j) for i in range(5) for j in range(5) if i % 2 == 0 and j % 2 != 0]
# print(result)
#
# result = [(i, j) for i in range(5) if i % 2 == 0 for j in range(5) if j % 2 != 0]
# print(result)


# 范例4：list1 = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]  -->[3,6,9,5]
# lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
# result = [i[2] for i in lists]
# print(result)
#
# def func():
#     newlist = []
#     for i in lists:
#         newlist.append(i[2])
#     return newlist
# result = func()
# print(result)
#

# dic1 = {'name': 'tom', 'salary': 4500}
# dic2 = {'name': 'lily', 'salary': 5500}
# dic3 = {'name': 'lucy', 'salary': 6500}
# dic4 = {'name': 'steven', 'salary': 3500}
#
# list1 = [dic1, dic2, dic3, dic4]
# # 薪资大于5000加200,低于等于5000加500；
#
# result = [i['salary'] + 200 if i['salary'] > 5000 else i['salary'] + 500 for i in list1]
#
# # print(result)
#
# def func(list1):
#     l = []
#     for i in list1:
#         if i['salary'] > 5000:
#             i['salary'] += 200
#             l.append(i)
#         else:
#             i['salary'] += 500
#             l.append(i)
#     return l
#
#
# # result = func(list1)
# # print(result)
#
#
# # lis = [7, 8, 9, 9, 2, 4, 7]
# # set1 = {i for i in lis if i > 5}
# # print(set1)
#
# dic = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}
# newdic = {value: key for key, value in dic.items()}
# print(newdic)


# g = (i*3 for i in range(3))
#
# while g:
#     try:
#         print(next(g))
#     except:
#         print('元素调用完毕！')
#         break

# def func():
#     n = 0
#     while n < 3:
#         n += 1
#         # print(n)
#         yield n
#
#     return '已调用完毕！'
#
# result = func()
# print(result)
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())

# def gen():
#     i = 0
#     while i < 5:
#         temp = yield i
#         print('temp', temp)
#         i += 1
#     return '没有更多的数据！'
#
#
# result = gen()
# print(result.__next__())
# # print(next(result))
# print(result.send(None))

# def gen():
#     i = 0
#     while i < 5:
#         temp = yield i  # return 0  + 暂停
#         print('temp', temp)
#         for x in range(temp):
#             print('------>', x)
#         print('**********', i)
#         i += 1
#     return '没有更多的数据！'
#
# g = gen()
# g.send(None)
# g.send(5)
# g.send(5)
# print(g.send(5))
# print(g.send(5))

# def func1():
#     for i in range(3):
#         print('看电影！')
#         yield
#
# def func2():
#     for i in range(3):
#         print('吃零食！')
#         yield
#
#
# g1 = func1()
# g2 = func2()
#
# while True:
#     try:
#         next(g1)
#         next(g2)
#     except:
#         print('任务完成！')
#         break

# from collections.abc import Iterable
#
# lis = [7, 8, 9, 9, 2, 4, 7]
# result = isinstance(lis, Iterable)
# print(result)

# class Person:
#     def __init__(self, name,age):
#         self.age = age
#         self.name = name
#
#
#     def __str__(self):
#         return f'__str__所返出来的内容：分别是{self.name}和{str(self.age)}'
#
# p = Person('jack',18)
# print(p)
# # 如果单纯打印对象名称，得到内存空间地址，对于开发者意义不大，
# # 所以如果想打印对象名的时候能够给开发者更多一些信息量；
# p1 = Person('Tom',30)
# print(p1)

# class Student:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         self.__score = 59
#
#     def __str__(self):
#         return f'{self.__name}今年已经{self.__age}岁，语文分数为：{self.__score}'
#
#     def setAge(self, age):
#         if age > 0 and age <= 80:
#             self.__age = age
#         else:
#             print('年龄不在规定的范围内，规定范围：0～80之间')
#
#     def setScore(self, score):
#         if score <= 100 and score > 0:
#             self.__score = score
#         else:
#             print('分数范围0-100之间，请核对是否正确！')
#
#     def getAge(self):
#         return self.__age
#
#     def getScore(self):
#         return self.__score


# s = Student('lily', 19)
# print(s)
# s.setScore(88)
# s.setAge(200)
# print(s)
# print(s.getAge())
# print(s.getScore())


# print(dir(Student))
# print(dir(s))
# print(s.__dir__())

# class Student:
#     def __init__(self, name, age):
#         self.__age = age
#         self.name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#
# s = Student('lily', 20)
# s.name = 'haha'
# print(s.age)
#
# s.age = 30
# print(s.age)
# print(s.name)


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#
# p = Person('lucy', 25)
# print(p.name)
# p.name = 'lily'
# print(p.name)
# print(dir(p))

# import random
#
#
# class Road():
#     def __init__(self, name, length):
#         self.name = name
#         self.length = length
#
#
# class Car():
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
#
#     def get_time(self, road):
#         run_time = random.randint(1, 10)
#         msg = f'{self.brand}品牌的车在{road.name}上以{self.speed}速度行驶{run_time}小时'
#         print(msg)
#
#     def __str__(self):
#         return f'{self.brand}品牌的，速度：{self.speed}'
#
#
# r = Road('京藏高速', 12000)
# r.name = '京哈慢速'
#
# audi = Car('奥迪', 120)
# audi.get_time(r)
#
# class Student():
#     def __int__(self,name,age):
#
#     pass
#
# class Book():
#     def __init__(self,name, ):
#     pass
#
# class Computer():
#     pass
#

# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self,a):
#         print(f'{self.name}正在吃饭')
#
#     def run(self):
#         print(f'{self.name}正在跑步！')
#
# class Student(Person):
#     def __init__(self, name, age, clazz):
#         super().__init__(name, age)
#         self.clazz = clazz
#
#     def study(self, course):
#         print(f'{self.name}正在学习{course}课程！')
#
#     def eat(self, food):
#         super().eat(a)
#         print(f'{self.name}正在吃。。。东西！--{food}好好吃！！')
#
# class Employee(Person):
#     def __init__(self, name, age, salary, manager):
#         super().__init__(name, age)
#         self.salary = salary
#         self.manager = manager
#
# class Doctor(Person):
#     def __init__(self, name, age, patients):
#         super(Doctor, self).__init__(name, age)
#         self.patients = patients
#
# s = Student('xiaoxiao', 18, 'NTD1910')
# s.run()
# s.study('Python')
# s.eat('螺丝粉')
#
# e = Employee('haha', 25, 35000, 'lilei')
#
# lis = ['lily', 'lucy', 'gaga']
# d = Doctor('jack', 36, lis)
#
# class Base:
#     def test(self):
#         print('---------base------')
#
#
# class A(Base):
#     def test(self):
#         print('----AAAAA')
#
#
# class B(Base):
#     def test(self):
#         print('-----BBBB')
#
#
# class C(Base):
#     def test(self):
#         print('------cccc')
#
#
# class D(A, B, C):
#     pass
#
#
# c = C()
#
# d = D()
# d.test()
# import inspect
# print(inspect.getmro(D))
#
# print(D.__mro__)

# 经典类
# class P1:
#     def foo(self):
#         print 'p1--foo'
#
#
# class P2:
#     def foo(self):
#         print 'p2--foo'
#
#     def bar(self):
#         print 'p2--bar'
#
#
# class C1(P1, P2):
#     pass
#
#
# class C2(P1, P2):
#     def bar(self):
#         print 'C2--bar'
#
#
# class D(C1, C2):
#     pass
#
#
# d = D()
# d.foo()  # 输出p1-foo
# d.bar()  # 输出P2--bar

# class A:
#     def __init__(self,name,age):
#         self.age = age
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,name):
#         self.__name = name
#
#
# a = A('lily',19)
# print(a.name)
# a.name = 'gege'
# print(a.name)


# class Person:
#     role = 'Pet'
#
#     def __init__(self, name):
#         self.name = name
#     def feed_pet(self, pet):  # pet既可以接收cat，也可以接收dog，还可以接收tiger
#         # isinstance(obj, 类)  ---> 判断obj是不是类的对象或者判断obj是不是该类子类的对象
#         if isinstance(pet, Pet):
#             print(f'{self.name}喜欢养宠物{pet.nickname}：')
#         else:
#             print('不是宠物类。。。 。。。')
# class Pet:
#     role = 'Pet'
#
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age
#
#     def show(self):
#         print(f'昵称：{self.nickname},年龄：{self.age}')
#
# class Cat(Pet):
#     role = '猫'
#
#     def catch(self):
#         print('抓老鼠... ...')
#
# class Dog(Pet):
#     role = '狗'
#
#     def watch_house(self):
#         print('看家高手... ...')
#
# class Tiger:
#     def eat(self):
#         print('太可爱了... ...')
#
# cat = Cat('花花', 2)
# dog = Dog('大黄', 3)
# person = Person('家伟')
# person.feed_pet(cat)
# pet    父类    cat   dog  子类
# pet   大类型   cat  dog 小类型


# class Singleton():
#     # 私有化
#     __instance = None
#
#     # 重写__new__
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#             print('---1')
#             return cls.__instance
#         else:
#             print('---2')
#             return cls.__instance
#
#
# s = Singleton()
# print("I'm s-->:", s)
#
# s1 = Singleton()
# print("I'm s1-->", s1)

# class Singleton():
#     __instance = None
#
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         return cls.__instance
#
#
# s = Singleton()
# s1 = Singleton()
# print(s)
# print(s1)

# class Person():
#     def __init__(self, name):
#         self.name = name
#
#     def feed_pet(self, pet):
#         if isinstance(pet, Pet):
#             print(f'{self.name}已将{pet.name}成功收养！')
#         else:
#             print(f'{pet.name}不是宠物。。。')
#
#
# class Pet():
#     def __init__(self,name):
#         self.name = name
#
#
#
# class Cat(Pet):
#     pass
#
#
# class Dog(Pet):
#     pass
#
#
# class Chicken():
#     def __init__(self,name):
#         self.name = name
#
#
# p = Person('lily')
# c = Cat('花花猫')
# ck = Chicken('鸡鸡')
# d = Dog('狗狗')
#
# p.feed_pet(ck)
# p.feed_pet(d)

# class Student():
#     def __init__(self, name):
#         self.name = name
#
#
#     def study(self,computer):
#         print(f'{self.name}经常使用{computer.name}来学习！')
#
#
# class Book():
#     def __init__(self, name):
#         self.name = name
#
#
# class Computer():
#     def __init__(self, name, style, color):
#         self.name = name
#         self.style = style
#         self.color = color
#
#     def work(self):
#         print('自动完成下载工作！')
#
#
# b = Book('大学语文')
#
# c = Computer('苹果', '平板', '红色')
# s = Student('小文')
# s.study(c)

# class Worker:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#
#     def __str__(self):
#         return f'age is：{self.age}'
#
# w = Worker('lily',30)
# print(w)

# __all__ = ['synFlood']
# import test2
# from test1 import *
# # from test import *

# synFlood('192.168.101.101','80')

# print(a)

# t = test1.A('lily', 20)
# t.run()
# a = test2.students
#
# print(a)
# import sys
# import datetime
# print(sys.argv[0])
# import time
# print(time.time())
# print(time.ctime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(datetime.date.today())

# timedel = datetime.timedelta(days=5)
# # print(timedel)
#
# now = datetime.datetime.now()
# # print(now)
#
# result = now - timedel
# print(result)
# now = datetime.datetime.now()
# cha = datetime.timedelta(days=7)
# print(now - cha)
# import time
# import random
# import hashlib

# result = random.random()  # 0~1之间的随机小数
# print(result)
#
# result1 = random.randrange(1, 10, 2)  # randrange(start,stop,step) 1~10 step--->1,3,5,7,9
# print(result1)
#
# result2 = random.randint(1, 10) # Return random integer in range [a, b], including both end points.
# print(result2)
#
# lis = ['lily', 'lucy', 'xiaoming', 'xiaohei']
# result3 = random.choice(lis)  # 随机获取列表中的元素
# print(result3)
#
# pai = ['黑桃K', '红心2', '方块9', '梅花A', '黑桃8', ]
# random.shuffle(pai)  # 随机打乱列表内元素的顺序
# print(pai)
#
# print(chr(65))
# print(ord(o'上'))

# msg = '一会一起吃午饭'
# md5 = hashlib.md5(msg.encode('utf-8'))
# print(md5.hexdigest())
#
# sha256 = hashlib.sha256(msg.encode('utf-8'))
# print(sha256.hexdigest())

# import pillow

# import sys
# import datetime


# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def run(self):
#         print('gogogoo')
#
#
# class B(A):
#     co = 'new'
#     def __init__(self, name, age, color):
#         self.color = color
#
#         super().__init__(name, age)
#
#     def run(self):
#         print('NONONONO')
#
#     @classmethod
#     def test(cls):
#         print(cls.co)
# b = B('name',18,'red')
# b.test()
#
# import os
#
# # print(os.listdir('/root'))
#
# print(os.path.dirname(__file__))
#
# print(os.path.isfile('/root/test.txt'))
# print(os.path.isabs('test.txt'))
# print(os.path.split('/root/test.txt'))
# print(os.path.join('/root/','abc.txt'))
# print(os.path.splitext('/root/test.txt'))
# print(os.getpid())
# print(os.getcwd())
# print(os.read())































