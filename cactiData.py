

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


