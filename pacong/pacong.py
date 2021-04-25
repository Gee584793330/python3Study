# coding=utf-8
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    # 爬取网页
    dataList = getData(baseUrl)
    savePath = ".\\豆瓣电影Top250"
    # 保存数据
    # saveData(savePath)
    askUrl("https://movie.douban.com/top250?start=0")

# 获取网页
def getData(baseUrl):
    dataList = []
    # 解析数据
    for i in range(0,10): #调用获取页面信息的函数：10次【左闭右开】
        url=baseUrl+str(i*25)
        html=askUrl(url)    #保存获取到的网页源码
    #逐一进行解析



    return dataList


# 获取一个指定网页内容
def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""

    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def saveData(dbpaht):
    return


if __name__ == "__main__":  # 当程序进行执行时
    # 调用函数
    main()
