import urllib
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re


def htmlinfo_extraction(URL):
    url = URL
    header = {
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }   #头部信息
    request = urllib.request.Request(url,headers=header)
    reponse = urllib.request.urlopen(request).read()

    soup = BeautifulSoup(reponse, 'html.parser')

    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式

    # print(soup.prettify())


    # 提取网页所有链接
    linklist = []
    linkstr = ' '
    for link in soup.find_all('a'):
        all_link = link.get('href')
        absolute_link = re.findall(pattern, all_link)
        if len(absolute_link) !=0:
            linklist.append(absolute_link[0])
            linkstr = linkstr + absolute_link[0] + ' '


    # 提取网页所有图片
    piclist = []
    picstr = ' '
    for pic in soup.find_all('img'):
        all_pic = pic.get('src')
        absolute_pic = re.findall(pattern, all_pic)
        if len(absolute_pic) !=0:
            piclist.append(absolute_pic[0])
            picstr = picstr + absolute_pic[0] + ' '


    # 提取网页所有脚本
    scriptlist = []
    scriptstr = ' '
    for script in soup.find_all('script'):
        javascript = script.get('src')
        if javascript != None:
            scriptlist.append(javascript)
            scriptstr = scriptstr + javascript + ' '


    # 提取页面关键词
    for meta in soup.find_all('meta'):
        if meta.get('name') == "keywords":
            keyword = meta.get('content')


    # 提取网页所有文字内容
    html_text = soup.get_text()


    # 提取页面标题
    html_title = soup.title.string


    # print(soup.title)
    # print(soup.title.name)
    # print(soup.title.parent.name)
    # print(soup.p)
    # print(soup.p['class'])
    # print(soup.a)

    return linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title


# url = 'https://www.douban.com/'  # 菜鸟教程搜索页面
# linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title = htmlinfo_extraction(url)
# print(picstr)