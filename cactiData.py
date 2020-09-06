

import re


# with open("C:\\Users\\75222\Desktop\\'18中 - 流量 - Gi0_7'.csv",'rb+') as r:
#     result = r.read().decode('utf-8')
#
#
# partian = re.compile(r'2020-0\d-\d+ 08:00:00","(.*?)","(.*?)"',re.S)
# r = re.findall(partian,result)
# print(r)
# intList = []
# outList = []
# for i in r:
#     intList.append(i[0])
#     outList.append(i[1])
#
# newList = []
# for l in outList:
#     l = float(l)
#     newList.append(l)
# print(len(newList))
#
# s = sum(newList)
# mx = max(newList)
# print('最大：',mx/1024/1024)
# print('平均：',s/1024/1024/len(newList))

# ------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


from PIL import Image
import os
import pytesseract
import requests
import re
import json
import time
#
#

# 获取图片的ID号
def getNum(url):
    headers = {
        'Cookie':"Cacti=9gh0d3u7dsvqb4o03c5m4j4bq4; clickedFolder=tree_1%5Etree_6%5Etree_6_leaf_267%5Etree_6_leaf_266%5Etree_6_leaf_286%5Etree_6_leaf_519%5E; highlightedTreeviewLink=tree_6_leaf_519; ray_leech_token=159842954",
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
    responses = requests.get(url, headers=headers)
    html = responses.text
    # print(html)
    # 获取接口名和对应的ID
    # pattern = re.compile(r".*?Gi0/7'>(.*?)</a>.*?<td.*?'>(\d+)</td>",re.S)
    # 获取到ID号-->list
    pattern = re.compile(r".*?Gi0/7'>.*?</a>.*?<td.*?'>(\d+)</td>", re.S)
    results = re.findall(pattern,html)
    # print(results)
    for result in results:
        # print(result,'yield')
        yield result
    # items = {}
    # for i in result:
    #     items[i[0]] = i[1]
    # print(items)
    # with open('C:\\Users\\75222\Desktop\\imgNub.txt','a+') as w:
    #     w.write(str(items))


# 获取图片，并保存至文件夹；
def getImg(numbers):
    headers = {
        'Cookie': "Cacti=9gh0d3u7dsvqb4o03c5m4j4bq4; clickedFolder=tree_1%5Etree_6%5Etree_6_leaf_267%5Etree_6_leaf_266%5Etree_6_leaf_286%5Etree_6_leaf_519%5E; highlightedTreeviewLink=tree_6_leaf_519; ray_leech_token=159842954",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    for i in numbers:
        # print(i,'Img')
        Imgurl = 'http://10.80.46.4/graph_image.php?action=view&local_graph_id={}&rra_id=3'.format(i)
        responses = requests.get(Imgurl,headers=headers)
        imgs = responses.content

        with open(r'G:\img\{}.png'.format(i), 'wb') as w:
            w.write(imgs)

def main():
    for i in range(1,12):
        url='http://10.80.46.4/graphs.php?filter=&host_id=-1&page={}'.format(i)
        numbers = getNum(url)
        getImg(numbers)
# main()

# 获取图片信息
def getMsgMax():
    msgsListMax = []
    msgASG = []
    imgList = os.listdir(r'G:\img')
    for i in imgList:
    #     print(i)
        img = Image.open(r'G:\img\{}'.format(i))
        text = pytesseract.image_to_string(img,lang='chi_sim')
        # print(text)

        # pattern = re.compile('(.*?)\s.*?(流入).*?\s平均，(.*?M)\s最大\s(.*?M).*?(流出).*?平均\s(.*?)\s最大(.*?)\n',re.S)
        # pattern =  re.compile('(.*?)\s-.*?最大(.*?)\n.*?最大(.*?)\n',re.S)
        pattern = re.compile('(.*?)\s-.*?平均(.*?)最大.*?平均(.*?)最大',re.S)
        result = re.findall(pattern,text)
        print(result)
        # msgsListMax.append(result)
        msgASG.append(result)
    # print(msgsList)
    for i in msgASG:
        # print(i)
        with open('G:\ASG.txt','a+') as w:
            w.write(str(i))

# getMsgMax()
# with open('G:\\ASG.txt') as r:
#     asg = r.read()
# print(asg)
# a = asg.split(']')
# print(len(a))
# newList = []
# for i in a:
    # print(i)
    # ls = i.strip('[')
    # ls.strip('')
    # print(ls.strip(')'))
    # print(ls.strip("''"))
    # ls1 = i.strip()
    # print(ls)
    # newList.append(ls)

# newLists = ''.join(newList)
# print(newList)

# for j in newList:
#     print(j)

lists = """
[('元岗小学', '。 644 M', ' 359.57k')]
[('先烈东小学', '9.95 M', '2.87 M')]
[('天河第一4学华利校区', ' 61.41 M', '，18.80 M')]
[('洗村小学', ' 1379 M', '3.21 M')]
[('凌塘小学', '9.98 M', ' 941 45k')]
[('前进小学', ' 12.50 M', ' 129 M')]
[('华景小学北校区', ' 13.85 M', '， 529 M')]
[('华景小学南校区', ' 3.46M', ' 379 M')]
[('华融小学', '51.08 M', '。 5.48 M')]
[('南国学校', ' 3467 M', '52.65 M')]
[('员村小学美林校区', ' 1175 M', '167 M')]
[('员村小学三横路校区', ' 9.65 M', '2.12 M')]
[('海小学', ' 1424M', ' 231 M')]
[('天府路小学', ' 2335 M', ' 375 M')]
[('天河启起学校', '4.69 M', '，2438 M')]
[('天河实验幼儿园', '8.23 M', '3.49 M')]
[('天河实验幼儿园各东园区', '779 M', '335 M')]
[('天河第三实验幼儿园', '9.84 M', '179 M')]
[('天河第二实验幼儿园', '3.17 M', '1.10 M')]
[('御景小学', ' 23.60M', '270M')]
[('新元小学', '8.89 M', '1.62 M')]
[('新塘小学', ' 820M', ' 1832 M')]
[('旭景小学', '。 8.83 M', '， 458 M')]
[('柯木盟小学', '，7.55 M', ' 62660k')]
[('棠下4学', '， 4.58 M', '123 M')]
[('棠东小学', ' 11.50 M', '”8.09 M')]
[('棠德南小学', '38.71 M', ' 420 M')]
[('棠德南小学北校区', '1.87 M', '1.88 M')]
[('沐陵学', ' 1446 M', '，3.22 M')]
[('少年官', ' 1114 M', ' 7.16 M')]
[(' \n\n岑村小学', '， 2.98 M', ' 80632k')]
[('沙河4学', '713 M', ' 626M')]
[('泰安4学', ' 1378 M', '5.29 M')]
[('泰安中学', '”4330 M', ' 1003 M')]
[('渔沙坦小学', ' 18.01 M', '， 485 M')]
[('车陵小学', '，17.27 M', '132 M')]
[('龙岗路小学', ' 8.94M', '， 2.13 M')]
[('89中', ' 17.51 M', '575 M')]
[('盈彩美居4学', '7.84 M', '“234 M')]
[('下东徐', '。 8.64 M', ' 347.82k')]
[('长兹4学', ' 12.25 M', '446 M')]
[('骏景小学', ' 2109k', ' 112 M')]
[('高塘石小学', '， 5.49 M', '3.58 M')]
[('财务结算中心', ' 4676 M', '496 M')]
[('吉山4只', '33.02 M', '7.23 M')]
[('华康学', ' 25.59 M', ' 5.60 M')]
[('华师附中初中部 ( 113中五山校区 )', '27.43 M', '。 2.64 M')]
[('虽乐4学', ' 21.83 M', '。 8.13 M')]
[('广州中学凤凰校区', '93.84 M', ' 26479 M')]
[('银河小学橡树校区', '2.95 M', '3.23 M')]
[('侨乐4学北校区', ' 7.85 M', '147 M')]
[('体育西路小学-西校区', ' 1486 M', ':')]
[(' \n\n天漂      验几学', '”7.56M', '20.65 M')]
[(元岗小学东校区', '676M', ' 85416k')]
[('天府路小学翠湖校区', '7.14 M', '3.97 M')]
[('体育东小学珠江新城校区', ':', ':')]
[("五一说", ' 13.44M', '662 M')]
"""

r = re.compile(r"\[\('(.*?)'\)\]",re.S)
re.sub('.*?,',',',r)
rs = re.findall(r,lists)
print(type(rs))
for i in rs:
    print(i)
