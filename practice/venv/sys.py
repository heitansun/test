import json
import os
import re
import time

import pytesseract
import requests
from PIL import Image


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


# 获取图片的ID号
def getNum(url):
    headers = {
        'Cookie': "Cacti=9gh0d3u7dsvqb4o03c5m4j4bq4; clickedFolder=tree_1%5Etree_6%5Etree_6_leaf_267%5Etree_6_leaf_266%5Etree_6_leaf_286%5Etree_6_leaf_519%5E; highlightedTreeviewLink=tree_6_leaf_519; ray_leech_token=159842954",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    responses = requests.get(url, headers=headers)
    html = responses.text

    pattern = re.compile(r".*?Gi0/7'>.*?</a>.*?<td.*?'>(\d+)</td>", re.S)
    results = re.findall(pattern, html)
    # print(results)
    for result in results:
        yield result


# 获取图片，并保存至文件夹；
def getImg(numb):
    headers = {
        'Cookie': "Cacti=9gh0d3u7dsvqb4o03c5m4j4bq4; clickedFolder=tree_1%5Etree_6%5Etree_6_leaf_267%5Etree_6_leaf_266%5Etree_6_leaf_286%5Etree_6_leaf_519%5E; highlightedTreeviewLink=tree_6_leaf_519; ray_leech_token=159842954",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    for i in numb:
        # print(i,'Img')
        Imgurl = 'http://10.80.46.4/graph_image.php?action=view&local_graph_id={}&rra_id=3'.format(i)
        responses = requests.get(Imgurl, headers=headers)
        imgs = responses.content

        with open(r'G:\img\{}.png'.format(i), 'wb') as w:
            w.write(imgs)


def main():
    for i in range(1, 12):
        url = 'http://10.80.46.4/graphs.php?filter=&host_id=-1&page={}'.format(i)
        numb = getNum(url)
        getImg(numb)


# main()

# 获取图片信息
def getMsgAsg():
    outAsg = {}
    intAsg = {}
    imgList = os.listdir(r'/root/PycharmProjects/img')
    for i in imgList:
        img = Image.open(r'/root/PycharmProjects/img/{}'.format(i))
        text = pytesseract.image_to_string(img, lang='chi_sim')
        # print(text)

        pattern = re.compile('(.*?)\s-.*?平均(.*?)最大.*?平均(.*?)最大', re.S)
        result = re.findall(pattern, text)
        if result != []:
            key = result[0][0]
            intAsg[key] = result[0][1]
            outAsg[key] = result[0][2]
    print(outAsg, intAsg)
    return intAsg, outAsg


def clearAsg():
    outAsg, intAsg = getMsgAsg()
    for key, value in intAsg.items():
        # print(key)
        pattern = re.compile(r'(\d+.\d+)', re.S)
        resultReList = re.findall(pattern, value)
        try:
            v0 = float(resultReList[0])
            if v0 > 100:
                intAsg[key] = v0 / 100 * 1024
            else:
                intAsg[key] = v0 * 1024
        except Exception as err:
            pass
            # print(v0)

    for key, value in outAsg.items():
        # print(key)
        pattern = re.compile(r'(\d+.\d+)', re.S)
        resultReList = re.findall(pattern, value)
        try:
            v1 = float(resultReList[0])
            if v1 < 10:
                outAsg[key] = v1 * 1024
            elif v1 > 1000:
                outAsg[key] = v1 / 100
            else:
                outAsg[key] = v1
        except Exception as err:
            pass
    if os.path.isfile('/root/PycharmProjects/intASG.txt') == False:
        with open('/root/PycharmProjects/intASG.txt', 'a', encoding='utf-8') as w:
            w.write(json.dumps(intAsg, ensure_ascii=False) + '\n')

    if os.path.isfile('/root/PycharmProjects/outASG.txt') == False:
        with open('/root/PycharmProjects/outASG.txt', 'a', encoding='utf-8') as w2:
            w2.write(json.dumps(outAsg, ensure_ascii=False) + '\n')


# clearAsg()


# 获取图片信息
def getMsgMax():
    intMax = {}
    outMax = {}
    imgList = os.listdir(r'/root/PycharmProjects/img')
    for i in imgList:
        # print(i)
        img = Image.open(r'/root/PycharmProjects/img/{}'.format(i))
        text = pytesseract.image_to_string(img, lang='chi_sim')
        # print(text)

        pattern = re.compile('(.*?)\s-.*?最大(.*?)\n.*?最大(.*?)\n', re.S)
        result = re.findall(pattern, text)
        # print(result,type(result))
        if result != []:
            key = result[0][0]
            intMaxvalue = result[0][1]
            outMaxvalue = result[0][2]
            intMax[key] = intMaxvalue
            outMax[key] = outMaxvalue
        # print(intMax)
    return intMax, outMax


def clearMax():
    intMax, outMax = getMsgMax()
    # print(intMax, outMax)
    for key, value in intMax.items():
        pattern = re.compile(r'(\d+.\d+)', re.S)
        resultReList = re.findall(pattern, value)
        try:
            v0 = float(resultReList[0])
            if v0 < 300:
                intMax[key] = v0 * 1024
            elif v0 > 1000:
                intMax[key] = v0 / 100 * 1024
            else:
                intMax[key] = v0
        except Exception as err:
            pass
    print(intMax)

    for key, value in outMax.items():
        pattern = re.compile(r'(\d+.\d+)', re.S)
        resultReList = re.findall(pattern, value)
        try:
            v0 = float(resultReList[0])
            if v0 < 300:
                outMax[key] = v0 * 1024
            elif v0 > 1000:
                outMax[key] = v0 / 100 * 1024
            else:
                outMax[key] = v0
        except Exception as err:
            pass
    print(outMax)
    # if os.path.isfile('/root/PycharmProjects/intMax.txt') == False:
    #     with open('/root/PycharmProjects/intMax.txt', 'a', encoding='utf-8') as w:
    #         w.write(json.dumps(intMax, ensure_ascii=False) + '\n')
    #
    # if os.path.isfile('/root/PycharmProjects/outMax.txt') == False:
    #     with open('/root/PycharmProjects/outMax.txt', 'a', encoding='utf-8') as w:
    #         w.write(json.dumps(outMax, ensure_ascii=False) + '\n')


# clearMax()
