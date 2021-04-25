import urllib.request
import urllib.parse
#
# # 获取一个get请求
# # response=urllib.request.urlopen("http://www.baidu.com/")
# # print(response.read().decode('utf-8'))
#
# # 获取一个post请求
#
# # data=bytes(urllib.parse.urlencode({"Hello":"world"}),encoding="utf-8")
# #
# # resqonse=urllib.request.urlopen("http://httpbin.org/post",data=data)
# # print(resqonse.read().decode("utf-8"))
#
# try:
#     resqonse=urllib.request.urlopen("http://douban.com")
#     print(resqonse.read().decode("utf-8"))
#     print(resqonse.status)
#
# except urllib.error.URLError as e:
#     print("timeout")

# resqonse=urllib.request.urlopen("http://www.baidu.com")
# print(resqonse.getheader("server")

# url ="http://httpbin.org/post"
# headers={
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
# }
#
# data=bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
#
# req=urllib.request.Request(url=url,headers=headers,method="POST")
#
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url="https://www.douban.com"
headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"
}

req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
