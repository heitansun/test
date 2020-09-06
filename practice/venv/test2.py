# import random
# import time
#
# def login(username, password):
#     user = 'admin'
#     passwd = '123456'
#     for i in range(0, 2):
#         if username == user and password == passwd:
#             print('登录成功！')
#             break
#
#         else:
#             print('用户或密码错误，请重新输入！')
#             username = input('请输入用户名:')
#             password = input('请输入密码：')
#     print('账户锁定30分钟！')
#     time.sleep(10)
#
#
# username = input('请输入用户名:')
# password = input('请输入密码：')
#
# login(username, password)


# """
# 目标：使用函数创建一个列表或元组里面的最大值：
# 核心步骤：
# 1.创建函数；
# 2.实现的方法；
#     a.假设：[1,2,3,4,7,8] 比较 list[0]
#     b.如果 1 > list[0]
#     c. 将结果赋值给list[0]
# 3.执行函数，并传入list参数;
# 4.测试
# """
# import random
#
#
# # 获取随机列表
# def RanDom(num):
#     l = []
#     for i in range(0, num):
#         result = random.randint(0, 20)
#         l.append(result)
#     # print(l)
#     return l
#
#
# def Max(iteration):
#     for i in iteration:
#         if i > iteration[0]:
#             iteration[0] = i
#     print(iteration[0])
#
#
# def Min(iteration):
#     for i in iteration:
#         if i < iteration[0]:
#             iteration[0] = i
#     print(iteration[0])
#
#
# def Sort(iteration):
#     for i in range(len(iteration) - 1):
#         for j in range(0, len(iteration) - 1 - i):
#             if iteration[j] > iteration[j + 1]:
#                 iteration[j], iteration[j + 1] = iteration[j + 1], iteration[j]
#     result = set(iteration)
#     print(result)
#     return result
#
# def Reverse(iteration):
#     result = list(Sort(iteration))
#     r = result[::-1]
#     print(r)
#
#
# # lists = RanDom(20)
#
# lists = []
# for i in range(0,10):
#     l = int(input('请输入数字'))
#     lists.append(l)
#
# if isinstance(lists,tuple) or isinstance(lists,list):
#     Max(lists)
#     Min(lists)
#     Sort(lists)
#     Reverse(lists)
# else:
#     print('请输入正确的数字：')


# seq = ['one', 'two', 'three']
# for i, enumerate in list(enumerate(seq)):
#     print(i, enumerate)

# name = 'Runoob'
# print(f'{6+10=}')
# print(f'Hello {name}')
# seq = ("r", "u", "n", "o", "o", "b")
# print(type(seq))
# result = ''.join(seq)
# print(result)
#
# url = 'http://139.9.190.92:9000/note/'
# par = '5f34c73e2acb780e83000000'
# urls = f'ip address:{url+par}'
# print(urls)
# l1 = [1, 3, 5, 8, 9, 0]
# l2 = l1
# print(id(l2) == id(l1))
# l1.remove(5)
# print(l2)

# def func(**kwargs):
#     print(kwargs)
#
#
# dic1 = {'001': 'python', '002': 'java', '003': 'C语言'}
# func(**dic1)
# def func1(a, *args):
#     print(a, args)
#
#
# #
# func1(2, 3, 4, 5)
# # 2,(3,4,5)
#
# func1(2, [1, 2, 3, 4, 5])
# # 2,([1,2,3,4,5],)
#
# func1(5, 6, (4, 5, 6), 9)
#
#
# # 5,(6,(4,5,6),9)
#
#
# def func(a=1, b=2, c=3, **kwargs):
#     print(a, b, c, kwargs)
#
#
# func(1)
# # 1,2,3,{}

# courses = ['html', 'python', 'java', 'mysql']
#
#
# def func(name, *args):
#     if len(args) > 0:
#         for i in args:
#             print(f'{name}学过了{i}语言！')
#
#
# func('lily', *courses)

# def add(a, b):
#     result = a + b
#     print(result)
#     return 'aaaaaaa'
#
#
# add(1, 1)
# x = add(1, 10)
# print(x)
# def add(a, b):
#     result = a + b
#     print(result)
#     return 'hello', 100
#
#
# a = add(1, 2)
# x, y = add(1, 2)
# print(a)
# print(x)
# print(y)

# def a():
#     print('aaaaaaa')
#
#
# def b():
#     a()
#     print('bbbbbbbbbbb')
#
#
# def c():
#     b()
#     print('ccccccccccccc')
#
#
# c()

# """
# 1.用户登录
# 2.输入密码
# 3.输入验证码
# """

# islogin = False
#
#
# def add_shopping(goodsName):
#     global islogin
#     if islogin:
#         if goodsNanme:
#             print(f'{goodsName}添加成功！')
#     else:
#         result = input('用户未登录！请问是否需要登录？（y/n）')
#         if result == 'y':
#             islogin = login()
#             print(islogin)
#         else:
#             return None
#
#
# def login():
#     for i in range(0, 3):
#         username = input('请输入用户名：')
#         password = input('请输入密码：')
#         if username == 'admin' and password == '123456':
#             return True
#         else:
#             print(f'密码错误！还有{-i + 2}次，账户将锁定！')
#
#
# goodsNanme = input('请输入商品名称:')
#
# add_shopping(goodsNanme)

# """
# 1.用户登录
# 2.输入密码
# 3.输入验证码  --> 封装一个函数
# """
# import random
#
#
# def login():
#     username = input('请输入用户名：')
#     password = input('请输入密码：')
#     code = generate_Checkcode(4)
#     codes = input(f'{code}\n请输入验证码：')
#
#     if username == 'admin' and password == 'admin' and codes.lower() == codes.lower():
#         print('登录成功！')
#
#
# def generate_Checkcode(n):
#     # l = []
#     num = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM0123456789'
#     code = ''
#     for i in range(0, n):
#         # num = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM0123456789'
#         # nums = random.choice(num)
#         s = random.randint(0, len(num) - 1)
#         code += num[s]
#         # l.append(nums)
#     return code
#
#
# # generate_Checkcode()
# login()

# def func():
#     # 声明变量
#     n = 100  # 局部变量
#     list1 = [3, 6, 9, 5]  # 局部变量
#
#     # 声明内部函数
#     def inner_func():
#         nonlocal n
#         for index, i in enumerate(list1):
#             # 0 3
#             list1[index] = i + n
#
#         list1.sort()
#
#         # 修改n变量
#         n += 101
#
#     # 调用一下内部的函数
#     inner_func()
#
#     print(list1)
#
#
# func()
#
# """
# 1.读取系统文件；
# 2.request请求网站，并判断状态码；
# 3.将返回状态，区别保存在不同的文件中；
# """
# import requests
# import os
#
#
# def readFile():
#     with open('/root/test.txt') as stream:
#         files = stream.readlines()
#         # print(files)
#         return files
#
#
# def requesNet(files):
#     ok = []
#     no = []
#     for i in files:
#         # print(i)
#         results = requests.get(i)
#         # print(results.encoding)
#         if results.status_code == 200:
#             ok.append(i)
#         else:
#             no.append(i)
#     return ok, no
#
#
# def saveFile():
#     pass
#
#
# # f = '/root/test.txt'
# files = readFile()
# # print(type(files))
# ok, no = requesNet(files)
# print(f'{ok}is ok!{no} is no!')
# # print(r)

# 闭包

# def func(a, b):
#     c = 10
#
#     def inner_func():
#         s = a + b + c
#         print(f'相加之后的结果是：{s}')
#
#     return inner_func
#
#
# # 调用func
# ifunc = func(6, 9)  # ifunc就是inner_func    ifunc = inner_func
#
# # 调用
# ifunc()

# def func():
#     a = 100
#
#     def inner_func1():
#         b = 90
#         c = a + b
#         print(c)
#
#     def inner_func2():
#         inner_func1()
#         print('----------->', a)
#         return 'hello'
#
#     return inner_func2
#
#
# ff = func()  # ----
# f = ff()  # ---
# print(f)

# def generate_count():
#     container = [0]
#
#     def add_one():
#         container[0] = container[0] + 1
#         print(f'当前第{container}次访问。')
#
#     return add_one
#
#
# counter = generate_count()
# counter()
# counter()
# counter()

# def func(number):
#     a = 100
#
#     def inner_func():
#         nonlocal a, number
#
#         number += 1
#
#         for i in range(number):
#             a += 1
#         print('修改后的a', a)
#
#     return inner_func
#
#
# inner = func(5)
# inner()
# import sqlmap
#
#
# def decorate(func):
#     a = 100
#     print('Wrapper外层打印测试！')
#
#     def wrapper():
#         func()
#         print('-------刷油漆！')
#         print('-------铺地板！')
#         print('-------装门！')
#     print('Wrapper-->加载完成！')
#
#     return wrapper
#
# @decorate
# def house():
#     print('毛坯房！')
#
# # house()

# import time
#
#
# def decorate(func):
#     print('测试！')
#
#     def wrapper(name):
#         print('正在校验中...')
#         time.sleep(2)
#         print('校验完毕！')
#         func(name)
#
#     return wrapper
#
#
# @decorate
# def func1(n):
#     print('----1')
#
#
# func1('a')
#
#
# @decorate
# def func2(name):
#     print('----2')
#
#
# func2('a')
#
#
# @decorate
# def func3(students):
#     for stu in students:
#         print(stu)
#
#
# students = ['lily', 'tom', 'lucy']
# func3(students)

#
# """
# 1.三层装饰器；
# """
#
# def outer(n):
#     def decorate(func):
#         def wrapper(*args):
#             func(*args)
#             print('刷墙！')
#             print('铺地板！')
#             print(f'共装修了{n}次')
#
#         return wrapper
#     return decorate
#
# # @outer
# def func1(name):
#     print(f'{name}装修！')
#
# @outer(2)
# def func2(name):
#     print(f'{name}装修！')
#
# # func1('小红家')
# func2('小李家')
# import time
#
# islogin = False
#
#
# def isLogin(func):
#     def wrapper(*args, **kwargs):
#         global islogin
#         # login()
#         if islogin:
#             func(*args, **kwargs)
#         else:
#             islogin = login()
#             print(islogin)
#             func(*args, **kwargs)
#     return wrapper
#
#
# def login():
#     username = input('请输入帐号：')
#     password = input('请输入密码：')
#     if username == 'admin' and password == 'admin':
#         return True
#     else:
#         return False
#
#
# @isLogin
# def pay(money):
#     if islogin:
#         print(f'付款{money} 元')
#         time.sleep(2)
#         print(f'付款成功')
#
#
# # money = input('请选择输入的金额：')
# # pay(30)
# pay(500)

# 求出a中最大的值
# list1 = [{'a': 1010, 'b': 125}, {'a': 10, 'b': 115}, {'a': 178, 'b': 152}, {'a': 17, 'b': 159}]
#
# # r = max(list1, key=lambda x: x['a'])
# # print(r)
# #
# #
# # def lamdba(x):
# #     return x['a']
# #
# #
# # r2 = max(list1, key=lam)
# # print(r2)
#
# print(min(list1, key=lambda x: x['b']))

# 使用map()函数，将list1里面的值全部都加*5，


# data = [1, 2, 3, 68, 234, 8, 1, 3]
#
# def func(n):
#     return n * 5
#
#
# result1 = map(func, data)
# print(list(result1))
# #---------------------------------------
# result2 = (map(lambda n: n * 5, data))
# print(list(result2))

# from functools import reduce
#
# data = [1, 2, 3, 4]
# result = reduce(lambda x, y: x + y, data, 5)
# print(result)

# def func(n):
#     return n % 2 == 1


# iters = [1, 2, 3, 4]
#
# result = filter(lambda n: n % 2 == 1, iters)
# print(list(result))

# a = 7 % 2 == 0
# print(a)

# students = [
#     {'name': 'tom', 'age': 20},
#     {'name': 'lucy', 'age': 19},
#     {'name': 'lily', 'age': 22},
#     {'name': 'jack', 'age': 28},
#     {'name': 'steven', 'age': 10},
#
# ]

# result = sorted(students, key=lambda n: n['age'], reverse=False)
# print(result)

# def func(student):
#     return student['age'] > 20
#
#
# # result = filter(func, students)
# result = filter(lambda n: n['age'] > 20, students)
# print(list(result))

# students = [
#     {'name': 'tom', 'age': 20},
#     {'name': 'lucy', 'age': 19},
#     {'name': 'lily', 'age': 22},
#     {'name': 'jack', 'age': 28},
#     {'name': 'steven', 'age': 10},
#
# ]
#
# with open('/root/test.txt','a+') as stream:
#     result = stream.writelines(['hello','world','very good!'])
#
# print(result)
# import os
#
# file = os.open('/root/test.txt', os.O_RDWR)
# print(os.read(file, 4000))
# os.close(file)
# path = os.path.abspath('/root/test.txt')
# name = os.path.basename(path)
# print(path)
# print(name)

#  将/root/2.jpg 复制到opt目录下

# with open('/root/2.jpg', 'rb') as stream:
#     container = stream.read()
#
# with open('/opt/ooxx.jpg', 'wb') as wstream:
#     wstream.write(container)
#
# print('----ok-----')

# import os
#
# path = '/var/www/html/'
# dirs = os.listdir(path)
# for file in dirs:
#     print(f'{path}',file)

# data = [1, 2, 3, 4]
#
# def func(n):
#     return n * 5
#
# result1 = map(func, data)
# print(list(result1))

# print(list(result1))




