import requests
from bs4 import BeautifulSoup
import re1

url = "https://movie.douban.com/top250"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

resp = requests.get(url,headers=headers)



# 解析数据
# 1. 把页面源代码交给BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(resp.text,"html.parser") #指定html解析器
# print(page)

# 2.从bs对象中查找数据
# find(标签，属性=值)
# findall(标签，属性=值)
div = page.find_all("div",class_="grid_view") # class是Python的关键字

name = page.find_all("span",class_="title")
name =str(name)
print(name)
obj =re1.compile(r'<span class="title">(?P<title>.*?)</span>', re1.S)
result = obj.finditer(name)
for it in result:
    print(it.group("title"))


# score = page.find_all("span",class_="rating_num")
# review = page.find_all("span",class_="inq")
#
# print(name)
# print(score)
# print(review)
