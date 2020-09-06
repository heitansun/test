# from lxml import etree
# # from one import ClassTest
# import ClassTest
#
# # print(ClassTest)
# text = """
# <div>
# <ul>
# <li class="item-0" name="lily"><a href="link1.html">first item</a></li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-inactive"><a href="link3.html">thrid item</a></li>
# <li class="item-1"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>
# </ul>
# </div>
# """

# html = etree.parse('./test.html', etree.HTMLParser())
# html = etree.HTML(text)
# print(html.xpath('//li[contains(@class,"item-0") and @name="lily"]/a/text()'))

# c = ClassTest.Spider()
# url = 'https://maoyan.com/board/6'
# html = c.getRequest(url)
# print(html)
# parser = etree.HTML(html)
# result = parser.xpath('*//dl[@class="board-wrapper"]/dd')
# print(result)
# items = {}
# for i in result:
#     items['index'] = i.xpath('//i[contains(@class,"board-index")]/text()')
#     items['img'] = i.xpath('//a/img/@data-src')
#     items['name'] = i.xpath('//p[@class="name"]/a/text()')
#     items['star'] = i.xpath('//p[@class="star"]/text()')
#     items['time'] = i.xpath('//p[@class="releasetime"]/text()')
#
# print(items)

# //*[@id="app"]/div/div/div[1]/dl/dd[1]/i
# //*[@id="app"]/div/div/div[1]/dl/dd[2]/i


from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from: ', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (bytes(ctime(), "utf-8"), data))

    tcpCliSock.close()

# tcpSerSock.close



