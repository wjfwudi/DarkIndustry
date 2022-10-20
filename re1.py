# 爬取爬取域名 80 端口和 443 端口对应的 html 页面源代码

import requests
import re1

url = "https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的单词：")
dat = {"kw": s}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}

resp = requests.post(url,headers=headers,data=dat)
print(resp.json())
resp.close()

# findall: 匹配字符串中所有的符合正则的内容
lst = re1.findall(r"\d+", "我的电话号是：10086，我女朋友的电话号是：10010")
print(lst)


# fiinditer: 匹配字符串中所有内容（返回的是迭代器），从迭代器中拿到的内容需要.group()
it = re1.finditer(r"\d+", "我的电话号是：10086，我女朋友的电话号是：10010")
for i in it:
    print(i.group())

# search, 找到一个结果就返回，返回的结果是match对象，那数据需要.group()
s = re1.search(r"\d+", "我的电话号是：10086，我女朋友的电话号是：10010")
print(s.group())

# match是从头开始匹配
s1 = re1.match(r"\d+", "10086，我女朋友的电话号是：10010")
print(s1.group())

# 预加载正则表达式
obj = re1.compile(r"\d+")

ret = obj.finditer("我的电话号是：10086，我女朋友的电话号是：10010")
for it in ret:
    print(it.group())

ret = obj.findall("呵呵呵。我就不信你有10000000")
print(ret)

# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj =re1.compile(r'<span class="title">(?P<title>.*?)</span>', re1.S)
result = obj.finditer(resp.text)
for it in result:
    print(it.group("title"))
