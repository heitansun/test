# class Phone():
#     color = 'red'
#     banner = 'iphone'
#
# lily = Phone()
#
# print(lily.color)
# lily.color = 'blue'
# lily.shape = 'rectangle'
# Phone.color = 'greed'
# print(Phone.color,'----')
# print(lily.shape)
# print(lily.color)
#
#
#
# # 模型包含了属性也包含了方法
# class Phone:
#     brand = 'xiaomi'
#     price = 4999
#     type = 'mate 80'
#
#     def call(self):
#         print('self----->', self)
#         print('正在打电话... ...', self.address_book)
#
#
# # 创建实例p1==开辟了一个内存空间并指向“Phone模型”
# p1 = Phone()
# print(p1, '------p1----------')
# # 调用call方法。当调用call时，相当于把自己（p1及内存空间地址）作为参数，并赋值给了call方法的self
# p1.address_book = ['oo', 'xx']
# p1.call()
# # print('self----->', self)  -----是自己开辟的空间地址
# # print('正在打电话... ...')
#
# print('******************分割线***********************')
#
# # 创建实例p2==开辟了一个内存空间并指向“Phone模型”
# p2 = Phone()
# print(p2, '----------p2--------')
# # 调用call方法
# p2.call()
# # print('self----->', self)  ----->是自己开辟的空间地址
# # print('正在打电话... ...')


# class Phone:
#     def __init__(self):
#         self.name = 'lily'
#         print('------init-------', Phone.__init__)
#
#     def call(self):
#         print('-----self--->', self.name)
#
#
# p1 = Phone()
# p1.name = 'lilei'
# p1.call()
# print(p1)

# class Person(object):
#     name = '张三'
#
#     def __init__(self, age, name):
#         self.name = name
#         self.age = age
#
#     def eat(self, food):
#         print(f'{self.name}正在吃{food}！... ...')
#
#     def run(self):
#         print(f'{self.name},今年{self.age}岁，正在跑步')
#
#
# p1 = Person(25, '李五')
# p1.run()
#
# p2 = Person(35, '雷哥')
# p2.eat('叉烧')
#
# class Dog:
#
#     def __init__(self, nickname, age):
#         self.nickname = nickname
#         self.age = age
#
#     def run(self):
#         print(f'{self.nickname}在欢快的奔跑！')
#
#
#     def eat(self):
#         print('吃饭。。。。。。')
#         self.eat()  # 类中方法的调用，需要通过self.方法名()
#
#
#     @classmethod
#     def test(cls):
#         print(cls)
#         print('-------->')
#         # print(cls.nickname)
#
# d1 = Dog('大黄', 3)
# d1.run()
# d1.test()
# Dog.test()


# class Phone():
#     __brand = 'HUAWEI'
#
#     def __init__(self, color):
#         self.color = color
#
#     def style(self):
#         print(f'My Phone color is {self.color}!')
#         self.__brand = '三星'
#         print('brand is', self.__brand)
#
#     @staticmethod
#     def jintaifanfa():
#         Phone.__brand = 'Iphone'
#         print(f'My Phone is {Phone.__brand},it very Good!')
#
#
# p = Phone('red')
# p.style()
#
# Phone.jintaifanfa()
# Phone.style()

import requests
from requests.exceptions import RequestException
import re
import os
import json
import time
from random import random


# 1、抓取页面
# 2、正则提取
# 3、写入文件
# 4、分页爬取

class Spider():
    pass

    def __init__(self):
        # self.url = url
        pass

    def getRequest(self, url):
        try:
            headers = {
                'Host': 'maoyan.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep - alive',
                'Referer': 'https://maoyan.com/board',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
            }
            responses = requests.get(url, headers=headers)
            if responses.status_code == 200:
                return responses.text
            else:
                return None
        except RequestException:
            return None

    def pattern(self, html):
        pattern = re.compile(
            r'<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
            re.S)
        items = re.findall(pattern, html)
        # print(results)
        for item in items:
            yield {
                'index': item[0],
                'image': item[1],
                'title': item[2].strip(),
                'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
                'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
                'score': item[5].strip() + item[6].strip()
            }

    def saveFile(self, content):
        # print(content)
        with open('/root/t.txt', 'a', encoding='utf-8') as w:
            w.write(json.dumps(content, ensure_ascii=False) + '\n')

    def main(self, page):
        url = f'https://maoyan.com/board/4?offset={page}'
        html = self.getRequest(url)
        # print(html)
        print(self.pattern(html))
        for item in self.pattern(html):
            print(item)
            self.saveFile(item)


if __name__ == '__main__':
    s = Spider()
    for i in range(0, 100, 10):
        # print(i)
        s.main(i)
        time.sleep(1.25)

import sys
# print(sys.argv)