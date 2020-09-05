# def checkLogin(func):
#     def inner():
#         print("登录验证...")
#         func()
#     return inner
#
# @checkLogin
# def fss():
#     print("发说说")
# # fss = checkLogin(fss)
#
# @checkLogin
# def ftp():
#     print("发图片")
# # ftp = checkLogin(ftp)
#
# btnIndex = 1
# if btnIndex == 1:
#     fss()
# else:
#     ftp()
#


# 装饰器带参数
# """
# 带参数的装饰器是三层的；
# 最外层的函数是负责接收装饰器参数；
# 里面的内容还是原装饰器的内容；
# """
# def outer(a): # 第一层 ：负责接受装饰器的参数
#     def decorate(func): # 第二层 ： 负责接受函数的
#         def wrapper(*args, **kwargs): # 第三层 负责接受函数的参数
#             func(*args, **kwargs)
#             print("---->铺地板{}".format(a))
#         return wrapper  # 返出来：第三层
#     return decorate  # 返出来： 第三层
#
#
# @outer(10)
# def house(time):
#     print("我们{}日期拿到了房子，是毛毛坯房...".format(time))
#
# @outer(100)
# def street():
#     print("新修建街道叫：xxx路")
#
# house('2019-10-1')
# street()


# import time
# islogin = False # 默认没有登录
#
# # 定义一个登录函数
# def login():
#     username = input("请输入帐号：")
#     password = input("请输入密码：")
#     if username == "admin" and password == "123456":
#         return True
#     else:
#         return False
#
# # 定义一个装饰器，目的为了校验是否有登录，如果没有则需要执行login操作：
# def login_required(func):
#     def wrapper(*args, **kwargs):
#         global islogin
#         print("------Pay-------")
#         # 验证用户是否登录
#         if islogin:
#             func(*args, **kwargs)
#         else:
#             # 跳转登录页面
#             print("用户没有登录，不能付款！")
#             islogin = login()
#             print("result:", islogin)
#     return wrapper
#
# # 定义一个付款执行函数
# @login_required
# def pay(menoy):
#     print("正在付款，付款金额为：{}".format(menoy))
#     print("付款中...")
#     time.sleep(2)
#     print('付款完成！')
#
# pay(100)
#
# pay(200)

# list1 = [3, 4, 6, 7, 8, 9, 0, 2, 5]
#
# result = map(lambda x: x if x % 2 == 0 else x + 1, list1)
# print(list(result))
#
# for index, i in enumerate(list1):
#     if i % 2 != 0:
#         list1[index] = i + 1
#
# print(list1)

# from functools import reduce
#
# tuple1 = (3, 5, 7, 8, 1, 6)
# result = reduce(lambda x, y: x + y, tuple1)
# print(result)
#
# tuple2 = (1,)
# result = reduce(lambda x, y: x + y, tuple2, 10)
# print(result)

# def add(a, b):
#     return a + b
#
# f = add(1, 2)
# print(f)
#
# s = lambda a, b: a + b
# f = s(1, 2)
# print(f)

# list1 = [12, 3, 4, 6, 56, 74, 8, 4, 3, 13, 2, 46, 5]
#
# result = filter(lambda x: x > 10, list1)
# print(list(result))
#
# # 底层原理：
# def func(list1):
#     list2 = []
#     for i in list1:
#         if i > 10:
#             list2.append(i)
#     return list2
#
# result = func(list1)
# print(result)


# students = [
#     {'name': 'tom', 'age': 20},
#     {'name': 'lucy', 'age': 19},
#     {'name': 'lily', 'age': 22},
#     {'name': 'jack', 'age': 28},
#     {'name': 'steven', 'age': 10},
#
# ]
# # 找出年龄大于20岁的学生
# result = filter(lambda x: x['age'] > 20, students)
# print(list(result))
#
# # 按照年龄从小到大排序,(reverse=True-->表示倒序)
# result = sorted(students, key=lambda x: x['age'], reverse=True)
# print(result)

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n - 1)
#
#
# result = sum(10)
# print(result)
#
# s = 0
# for i in range(11):
#     s += i
# print(s)
#
#
# def f1(n):
#     if n > 0:
#         print("--->", n)
#         f1(n - 1)
#     else:
#         print('--->', n)
#
#
# f1(5)

#
# stream = open('/root/test_php.txt', 'rt')
# # container = stream.read()
# # print(container)
#
# result = stream.readable()  # 判断是否可以读取 True  False
# print(result)
#
# while True:
#     line = stream.readline()  # 读取文件中的第一行；使用遍历可以将全部内容打印出来；
#     print(line)
#     if not line:
#         break
#
# lines = stream.readlines()  # 将读取到的值，保存到列表中；可以使用for循环将列表内容全部打印；
# print(lines)

# stream = open('/root/test_php.txt', 'w')
#
# s = """
# 你好！
#     关于你最近的改变，我已经察觉到，虽然你并没有表露出来，但从你的言情，可以感受到，你比以前快乐了，我觉得这是一件好事！嘎嘎！其实爱你的人很多，比如有：
# """
# result = stream.write(s)
# print(result)
#
# stream.writelines(['周星驰\n', '黎明\n', '刘德华\n', '等等...\n'])  # 不会自动换行，需自行添加换行符\n
# stream.write('还有\n,张学友\n、啦啦啦啦\n')
#
# stream.close()  # 释放资源


# import os
#
# with open('/root/1.jpeg', 'rb') as stream:
#     container = stream.read()  # 读取文件内容
#     print(stream.name)
#     file = stream.name
#     filename = file[file.rfind('/')+1:]  # 截取文件名
#
#     path = os.path.dirname(__file__)
#     path = os.path.join(path, '1,jpeg')
#
#     with open('/opt/1.jpeg', 'wb') as wstream:
#         wstream.write(container)
# print('文件复制完成！')
#

# 把/root/1.jpeg 复制到/opt/下面
# with open('/root/1.jpeg', 'rb')as stream:
#     container = stream.read()
#     print(container)
#
# with open('/opt/1.png', 'wb') as wstream:
#     wstream.write(container)

import os

# # 当前路径
# path = os.path.dirname(__file__)
# print(path)
# # print(os.path)
# # print(os.path.dirname("/root/a.PHp"))
#
# # 将当前路径 + 文件名字 = 路径+文件名字
# result = os.path.join(path, '1.png')

# print(result)

# with open('/root/2.jpg', 'rb') as stream:
#     container = stream.read()
#
# # print(stream.name)
# file = stream.name
# filename = file[file.rfind('\\')+1:]
# print(filename)
#
#
# path = os.path.dirname(__file__)
# path1 = os.path.join(path, filename)
#
# with open(path1, 'wb') as wstream:
#     wstream.write(container)


# str1 = "this is really a string example....wow!!!"
# print(str1.rfind('string'))
#
# print('亲爱的xxx\n', ' ', '请点击链接激活用户：')
#
#
# print('AAA',end='')
# print('BBB',end='')
# print('CCC',end='')


# message ="""
# 将整个模块(somemodule)导入，格式为：
# import somemodule
# 从某个模块中导入某个函数,格式为：
# from somemodule import somefunction
# """
# print(message)

# person = 'xx'
# address = '广州海珠区xx路xx号xx室'
# phone = 1888888888
# num = 5.12345
#
# print('收件人：{}, 收获人：{}, 联系方式：{}, 数量：{}' .format(person, address, phone, num))

# print("""
# **********************************
#          抓鱼达人
# *********************************
# """)
#
# username = input('输入用户名：')
# password = input('请输入密码：')
#
# print('%s请充值开启游戏！' % username)
#
# coins = input('充值金额：') # input键盘输入的都是字符串类型 即使输入的是500,也会添加'500'自动转换为字符串！
# coins = int(coins)
#
# print('{}充值成功！游戏币是：{}'.format(username, coins))

# ceng = 1
#
# while ceng <= 5:
#     cont = 1
#     while cont <= ceng:
#         print('*', end='')
#
#         cont += 1
#     ceng += 1
#     print()
# [:]


# strs = "hello world"
#
# # 逆序输出：world  --> dlrow
# print(strs[-1:-6:-1])
# # 正向输出hello
# print(strs[:6])
# # 逆序输出整个hello world
# print(strs[:])
# # 打印获取oll
# print(strs[2:6])
# # 打印llo wo
# print(strs[2:8])

# url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
# p = url.rfind('/')  # right find 从右侧检索/的位置，得出‘/’的位置
# print(p)
# filename = url[p + 1:]  # 使用切片获取'/'后面字符串，即自己想要的名字
# print(filename)
#
# # 获取图片的后缀名
# p = url.rfind('.')
# print(p)
# filename = url[p+1:]
# print(filename)

# s1 = 'index lucy lucky goods'
# result = 'R' in s1
# print(result)
#
# position = s1.find('R')  # 返回值是-1则代表没有找到
# print(position)
#
# position = s1.find('l')  # 如果可以找到则返回字母第一次出现的位置
# print(position)
#
# p = s1.find('l', position + 1, len(s1) - 5)  # 指定位置开始查找
# print(p)
# s1 = 'index lucy lucky goods'
# new1 = s1.replace(' ', '#')  # 将s1的空字符串替换成#号
# print(new1)
# new2 = s1.replace(' ', '', 2)  # 将s1的前两个空字符串替换成空
# print(new2)

# 编码
# msg = '上课了，认真听课！' # 中文的
#
# result = msg.encode('utf-8')
# print(result)
#
# # 解码
# m = result.decode('utf-8')
# print(m)

# filename = '笔记.doc'
# result = filename.endswith('doc') # filename是否以doc结尾的
# print(result)
#
# s = 'hello'
# result = s.startswith('he') # s是否以he开头的
# print(result)

# s = 'abcd'
# result = s.isalpha()
# print(result)
#
# s = '456456'
# result = s.isdigit()
# print(result)
#

# 1.输入数字；
# 2.判断输入的内容是否都是数字；
#     3.如果是将输入内容进行转换为int；
#     4.如果不是，让用户重新输入，

# sum = 0
# i = 5
# while i >= 3:
#     inputs = input("请输入数字：")
#     if inputs.isdigit():
#         result = int(inputs)
#         sum += result
#         print('输入的数字：{}'.format(inputs))
#         i -= 1
#     else:
#         print('请输入正确的数字：')
# print('sum=', sum)

# list1 = ['l', 'o', 'v', 'e']
# result1 = ''.join(list1)
# result2 = '-'.join(list1)
# print(result1)
# print(result2)
#
# s1 = 'hello world hello kitty'
# print(s1.count('h'))
# s2 = 'hello-world-hello-kitty'
# result1 = s1.split(' ',2)  # 以中间的空格为切割点，进行分割并形成列表
# result2 = s2.split('-', 2)  # 以中间的'-'为切割点，进行分割并形成列表
# print(result1)
# print(result2)
# result = [1, 2, 3] + [4, 5, 6]
# print(result)


# brands = ['hp', 'dell', 'thinkpad', '支持华为', 'lenove']
# for brand in brands:
#     # if brand == '支持华为':
#     if '华为' in brand:
#         brands[len(brand) - 1] = 'HUAWEI'
# print(brands)
#
# for i in range(len(brands)):
#     if '华为' in brands[i]:
#         brands[i] = 'HUAWEI'
#         break
# print(brands)

# 只要是hp & dell都要删除
# brands = ['hp', 'dell', 'thinkpad', '支持华为', 'lenove', 'hp', 'dell', 'hp', 'mac', 'dell']
#
# l = len(brands)  # 10
# i = 0
# while i < l:  # b[0]
#     if 'hp' in brands[i] or 'dell' in brands[i]:
#         del brands[i]
#         i -= 1
#         l -= 1
#     i += 1
# print(brands)

# n = 0
# brands = ['hp', 'dell', 'thinkpad', '支持华为', 'lenove', 'hp', 'dell', 'hp', 'mac', 'dell']
#
# for i in brands:
#     n += 1
#     if 'hp' in i or 'dell' in i:
#         print(n)
#         del brands[n - 1]
# print(brands)

# girls = []
#
# while True:
#     names = input('name:')
#     girls.append(names)
#     if 'Q' == names:
#         break
#
# print(girls)

# a = ['aa', 'bb', 'cc']
# a.insert(1, 'ooxx')
# print(a)


# import random

# lists = []
# for i in range(0, 100):
#     ran = random.randint(0, 20)
#     if ran not in lists and len(lists) < 10:
#         lists.append(ran)
#
# print(lists)


# 产生10个 不同的随机数
# lists = []
# while len(lists) < 10:
#     ran = random.randint(0, 20)
#     if ran not in lists:
#         lists.append(ran)

# print(lists)
# 找出列表中最大值
# n = 0
# for i in lists:  # [1..4..54.]
#     if i > lists[0]:
#         lists[0] = i
# print(lists[0])
#         # n += 1
#
# print(lists)


# 排序 --整体思路:
# 每得到一个最大的数字按先后顺序放入到新的列表中；

# new = []
#
# for i in lists:
#     for l in i:
#         if i > lists[0]:
#             lists[0] = i
#
# new.append(lists[0])
#
# print(new)
# sorted()


# numbers = [[1, 2], [2, 3, 4], [5, 6]]
# print(len(numbers))
# num = numbers[2]
# print(num[2])
# num

# """
# 类型转换:
# str()
# int()
# list() 将指定的内容转成列表
#
# s = 'abc'
# result = list(s)  # ['a','b','c']
#
# # iterable 可迭代的 for ... in里面可以循环就是可迭代的
# # 'abcdef'  ---> a b c
# for i in rang(s):
#     pass
# """

# print(enumerate(brands))


# 产生10个 不同的随机数

#
# myList = [4, 1, 7, 0]
# for i in range(len(myList) - 1):
#     for j in range(0, len(myList) - 1 - i):
#         if myList[j] > myList[j + 1]:
#             myList[j], myList[j + 1] = myList[j + 1], myList[j]
#
# print(myList)

# t5 = ('4', '4', '4', '1', '0', '8', '8', '8', '0', '0')
# # print(t5.count('1'))
# print(t5.index('1'))
#
# print(len(t5))

# t2 = (5, 8, 9)
# a, b, c = t2
# print(a, b, c)
#
# t1 = (2, 5, 8, 9, 7)
# a, *_, c = t1
# print(a, _, c)
#
# t3 = (9,)
# a, *b = t3
# print(a, b)

# t4, *t5 = (9, 4, 8, 6, 7)
# print(t5)
# print(*t5)

# dict1 = {'name': 'lily', 'age': 19, 'height': 175}
# print(dict1['height'])

# dict1 = {}
# dict1['brand'] = 'HUAWEI'
# dict1['brand'] = 'MI'
# dict1['type'] = 'p30 pro'
# dict1['price'] = 9000
# dict1['color'] = 'black'
# print(dict1)
#
# databases = []
# user = {}
# while True:
#     print('======欢迎注册========')
#     username = input('请输出用户名名：')
#     password = input('请输入密码：')
#     repassword = input('请再次输入密码：')
#     email = input('请输入邮箱：')
#     phone = input('请输入电话号码：')
#
#     if repassword == password:
#         user['username'] = username
#         user['password'] = password
#         user['email'] = email
#         user['phone'] = phone
#         databases.append(user)
#         print('恭喜注册成功！')
#         break
#
#     else:
#         print('两次密码不一致！')
#
# print(databases)

# users1 = [('username', username), ('password', password), ('email', email), ('phone', phone)]
# user = dict(users1)
# print(users1)


# 考试分数大于90分的人
# dic = {'小明': 92, '小文': 89, '小花': 95, '李磊': 75, 'lily': 78}
#
# result1 = dic2.pop('lily',100) # 字典中如果存在lily的key，则字典对应的键值
# print(result1)
#
# result2 = dic.pop('haha', 100) # 字典中没有haha的key，则返回 默认值（自定义100）
# print(result2)

# dic1 = {0: 'tom', 1: 'jack', 2: 'lucy'}
# dic2 = {0: 'lily', 4: 'ruby'}
#
# result = dic1.update(dic2)
# print(result)  # 无返回值，即None
# print(dic1) # dic1的0的value值，已经更新为dic2的0的value值；

# lis1 = ['aa', 'bb', 'cc']
# new_dict1 = dict.fromkeys(lis1)
# new_dict2 = dict.fromkeys(lis1, 10)
# print(new_dict1)
# print(new_dict2)

# set1 = {1, 2, 3, 4, 5, 1, 21, 3, 2, 3, 4, 5}

# print(set1)
#
# t1 = ('lily','lucy')
# set1.add(t1)
# print(set1)

# set1.update(t1)

# set1.remove('lily')
# set1.discard('lucy')
# print(set1)

# """
# 1.产生10个1～20的随机数，去除里面的重复项；
# 2.键盘输入一个元素，将此元素从不重复的集合中删除；
# """
#
# import random
#
# list1 = []
# for i in range(10):
#     num = random.randint(0, 20)
#     list1.append(num)
# set1 = set(list1)
# print(set1)
#
# inputs = int(input('请输入删除的数字：'))
# # set1.update(inputs)
# result = set1.discard(inputs)
# print(set1)

# s1 = {1, 2, 3, 4, 5, 6, 7}
# s2 = {1, 2, 3, 5, 8, 9, 10}
# binji1 = s1 | s2
# binji2 = s2.union(s1)
# print(binji1)
# print(binji2)


#
# s1 = {0, 1, 2, 3, 5, 9}
#
# print(s1, id(s1))
# s1.pop()
# print(s1, id(s1))

# import requests
# req = requests.get('https://www.baidu.com/')
# print(req.status_code)

# container = [0]
#
# container[0] = container[0]+1
# # print(container)
# # print(type(container))
# print(container[0])
#
# print(container[0]+2)
# a = [0]
# print(type(a[0]))
#
# print(a[0]+1)
#
# def fun():

# class A:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#
#     def run(self):
#         print('gogogogogo')
#
# a = A('lily',30)
# if __name__=='__main__':
#     a.run()
#

# import threading
# import queue
# import random
# import time
#
# def produce(q):
#     i = 0
#     while i < 10:
#         num = random.randint(1, 100)
#         q.put('生产者产生数据--->：%d' % num)
#         print('生产者产生数据--->：%d' % num)
#         time.sleep(1)
#         i += 1
#
#     q.put(None)
#     # 完成任务
#     q.task_done()
#
# def consume(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print('<---消费者获取到：%s' % item)
#         time.sleep(4)
#
#     # 完成任务
#     q.task_done()
#
# if __name__ == '__main__':
#     q = queue.Queue(10)
#     arr = []
#
#     # 创建生产者
#     th = threading.Thread(target=produce, args=(q,))
#     th.start()
#
#     # 创建消费者
#     tc = threading.Thread(target=consume, args=(q,))
#     tc.start()
#
#     th.join()
#     tc.join()

# import time
# from greenlet import greenlet
# import gevent
# from gevent import monkey
# monkey.patch_all()
#
#
# def a():
#     for i in range(5):
#         print('A' + str(i))
#         time.sleep(0.1)
#
#
# def b():
#     for i in range(5):
#         print('B' + str(i))
#         time.sleep(0.1)
#
#
# def c():
#     for i in range(5):
#         print('C' + str(i))
#         time.sleep(0.1)
#
#
# if __name__ == '__main__':
#     g1 = gevent.spawn(a)
#     g2 = gevent.spawn(b)
#     g3 = gevent.spawn(c)
#
#     g1.join()
#     g2.join()
#     g3.join()


import requests

