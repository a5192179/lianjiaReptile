# -*- coding: utf-8 -*-
# **************************************************************************
# *【Creat time】：2016-11-04 19:48          【Version】：0.0
# *【Writer】：LiShuai 461837929@qq.com
# *【Writer department】：
# *【Function】：
# *
# *输入：日期 str str_date
# *输出：假日标志位 int flag_holiday 0：不是假日，1：是假日，-1：出错
# *
# *【Description】：
# *只能判断本年度的
# *
# *-------------------------------------------------------------------------
# *【Modification】：****-**-** **：**       【Version】：*.*
# *
# *【Writer】：LiShuai 461837929@qq.com
# *【Writer department】：
# *【Function】：
# *
# *
# *
# *【Description】：
# *
# *
# *
# **************************************************************************
import urllib.request
import pandas as pd
import time
import datetime

def findKeyWordFromResponse(html, beginStr, beginTranslation, endStr, endStrTranslation):
    beginIndex = html.find(beginStr) + beginTranslation
    endIndex = html.find(endStr) + endStrTranslation
    keyWord = html[beginIndex:endIndex]
    return keyWord

def getKeyWordFromUrl(url, decode, beginStr, beginTranslation, endStr, endStrTranslation):
    """
    decode = 'GBK' 'utf-8'
    """
    try:
        response = urllib.request.urlopen(url)
    except Exception as e:
        print(Exception, ":", e)

    html = response.read()
    html = html.decode(decode)
    keyWord = findKeyWordFromResponse(html, beginStr, beginTranslation, endStr, endStrTranslation)
    return keyWord, html

def getResoldNumPriceAount():
    """
    """
    url = 'https://cd.lianjia.com/fangjia/'
    decode = 'utf-8'
    beginStr = 'target="_blank">在售房源'
    beginTranslation = len(beginStr)
    endStr = '套</a><a href="/chengjiao/'
    endStrTranslation = 0
    resoldNum, html = getKeyWordFromUrl(url, decode, beginStr, beginTranslation, endStr, endStrTranslation)
    resoldNum = int(resoldNum)

    beginStr = '最近90天内成交房源'
    beginTranslation = len(beginStr)
    endStr = '套</a></span>'
    endStrTranslation = 0
    resoldAmout = int(findKeyWordFromResponse(html, beginStr, beginTranslation, endStr, endStrTranslation))

    beginStr = '<span class="num">'
    beginTranslation = len(beginStr)
    endStr = '</span><span class="unit">'
    endStrTranslation = 0
    resoldPrice = int(findKeyWordFromResponse(html, beginStr, beginTranslation, endStr, endStrTranslation))
    return resoldNum, resoldAmout, resoldPrice

def getGaoXinResoldNumPriceAount():
    """
    """
    url = 'https://cd.lianjia.com/fangjia/gaoxin7/'
    decode = 'utf-8'
    beginStr = 'target="_blank">在售房源'
    beginTranslation = len(beginStr)
    endStr = '套</a><a href="/chengjiao/'
    endStrTranslation = 0
    resoldNum, html = getKeyWordFromUrl(url, decode, beginStr, beginTranslation, endStr, endStrTranslation)
    resoldNum = int(resoldNum)

    beginStr = '最近90天内成交房源'
    beginTranslation = len(beginStr)
    endStr = '套</a></span>'
    endStrTranslation = 0
    resoldAmout = int(findKeyWordFromResponse(html, beginStr, beginTranslation, endStr, endStrTranslation))

    beginStr = '<span class="num">'
    beginTranslation = len(beginStr)
    endStr = '</span><span class="unit">'
    endStrTranslation = 0
    resoldPrice = int(findKeyWordFromResponse(html, beginStr, beginTranslation, endStr, endStrTranslation))
    return resoldNum, resoldAmout, resoldPrice
    
def getTianfuResoldNumPriceAount():
    """
    """
    url = 'https://cd.lianjia.com/fangjia/tianfuxinqu/'
    decode = 'utf-8'
    beginStr = 'target="_blank">在售房源'
    beginTranslation = len(beginStr)
    endStr = '套</a><a href="/chengjiao/'
    endStrTranslation = 0
    resoldNum, html = getKeyWordFromUrl(url, decode, beginStr, beginTranslation, endStr, endStrTranslation)
    resoldNum = int(resoldNum)

    beginStr = '最近90天内成交房源'
    beginTranslation = len(beginStr)
    endStr = '套</a></span>'
    endStrTranslation = 0
    resoldAmout = int(findKeyWordFromResponse(html, beginStr, beginTranslation, endStr, endStrTranslation))

    beginStr = '<span class="num">'
    beginTranslation = len(beginStr)
    endStr = '</span><span class="unit">'
    endStrTranslation = 0
    resoldPrice = int(findKeyWordFromResponse(html, beginStr, beginTranslation, endStr, endStrTranslation))
    return resoldNum, resoldAmout, resoldPrice

def getRentNum():
    url = 'https://cd.lianjia.com/zufang/'
    decode = 'utf-8'
    # 已为您找到 <span class="content__title--hl">114370</span> 套
    beginStr = '已为您找到 <span class="content__title--hl">'
    beginTranslation = 39
    endStr = '</span> 套'
    endStrTranslation = 0
    rentNum, html = getKeyWordFromUrl(url, decode, beginStr, beginTranslation, endStr, endStrTranslation)
    rentNum = int(rentNum)
    return rentNum

def getGaoXinRentNum():
    url = 'https://cd.lianjia.com/zufang/gaoxin7/'
    decode = 'utf-8'
    # 已为您找到 <span class="content__title--hl">114370</span> 套
    beginStr = '已为您找到 <span class="content__title--hl">'
    beginTranslation = 39
    endStr = '</span> 套'
    endStrTranslation = 0
    rentNum, html = getKeyWordFromUrl(url, decode, beginStr, beginTranslation, endStr, endStrTranslation)
    rentNum = int(rentNum)
    return rentNum

def getTianFuRentNum():
    url = 'https://cd.lianjia.com/zufang/tianfuxinqu/'
    decode = 'utf-8'
    # 已为您找到 <span class="content__title--hl">114370</span> 套
    beginStr = '已为您找到 <span class="content__title--hl">'
    beginTranslation = 39
    endStr = '</span> 套'
    endStrTranslation = 0
    rentNum, html = getKeyWordFromUrl(url, decode, beginStr, beginTranslation, endStr, endStrTranslation)
    rentNum = int(rentNum)
    return rentNum

def saveLianJiaReptileData(date):
    dateStr = date.strftime("%Y-%m-%d")
    filePath = 'E:\Project\lianjiaReptile\Data\lianjiaReptile.xlsx'
    hisData = pd.read_excel(filePath, header=0)
    reptileResult = []
    reptileResult.append(dateStr)
    resoldNum, resoldAmout, resoldPrice = getResoldNumPriceAount()
    reptileResult.append(resoldNum)
    reptileResult.append(resoldAmout)
    reptileResult.append(resoldPrice)
    resoldNum, resoldAmout, resoldPrice = getGaoXinResoldNumPriceAount()
    reptileResult.append(resoldNum)
    reptileResult.append(resoldAmout)
    reptileResult.append(resoldPrice)
    resoldNum, resoldAmout, resoldPrice = getTianfuResoldNumPriceAount()
    reptileResult.append(resoldNum)
    reptileResult.append(resoldAmout)
    reptileResult.append(resoldPrice)
    rentNum = getRentNum()
    reptileResult.append(rentNum)
    rentNum = getGaoXinRentNum()
    reptileResult.append(rentNum)
    rentNum = getTianFuRentNum()
    reptileResult.append(rentNum)

    reptileResultPd = pd.Series(reptileResult, index = hisData.columns, name = dateStr)
    hisData = hisData.append(reptileResultPd)

    hisData.to_excel(filePath, index=False, header=True)

if __name__ == "__main__":
    while True:
        print('Day judge begin:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '.')
        today = datetime.date.today()
        saveLianJiaReptileData(today)
        # 休眠到第二天
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)  # 用今天日期加上时间差，参数为1天，
        startTime_Str = str(tomorrow) + ' 22:00:00'
        # 得到新时间的时间类
        timeArray = time.strptime(startTime_Str, "%Y-%m-%d %H:%M:%S")
        # 得到新时间是多少秒
        startTime = int(time.mktime(timeArray))
        now = time.time()
        delay = startTime - now
        time.sleep(delay)


