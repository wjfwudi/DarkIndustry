import urllib
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import ssl


def htmlinfo_extraction(URL):
    url = URL
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'Cookie': 'AEC=AakniGPStgBkE78oYqyNUWGnKvt78i97hfV89Q9M1Qfga3WpkcVoaONb16Q; OTZ=6738220_24_24__24_; DV=Q-AFApj3WM0gYIMZotJe81q5eO2OQBjiKlD-42UvvwIAAAA; NID=511=VZCPeWmnoWY__R9euAw8DYLgdEl82NMiD-xnUIUO0yDS1OoLOjp4xydWKDf9Bs0yBs9dHPk3Aa3cho_t923bwGxW47Sv8bga2QhZsKpbPHmGJjYqJDltvsFFRQIYI2dZ4ivRTMvaOg5QhpTBLuFDKMlgKQV15GUOE4J85jmTjG2v8SuL-90_VhQVZvLMpN6kjMarKhbnIA; 1P_JAR=2022-10-24-07'
    }  # 头部信息
    ssl._create_default_https_context = ssl._create_unverified_context  # 关闭https的认证
    try:
        access_flag = 1  # 网页是否可访问
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
            if all_link != None and len(all_link) != 0 and (all_link[0] != 'h' or all_link[1] != 't' or all_link[2] != 't' or all_link[3] != 'p') and all_link[0] == '/':   # 将网页的相对链接补充完整
                all_link = url + all_link
            absolute_link = re.findall(pattern, str(all_link))     # 将非网页链接剔除出去
            if len(absolute_link) != 0:
                linklist.append(absolute_link[0])
                linkstr = linkstr + absolute_link[0] + ' '

        # 提取网页所有图片
        piclist = []
        picstr = ' '
        for pic in soup.find_all('img'):
            all_pic = pic.get('src')
            if all_pic != None and len(all_pic) != 0 and (all_pic[0] != 'h' or all_pic[1] != 't' or all_pic[2] != 't' or all_pic[3] != 'p') and all_pic[0] == '/' :   # 将网页的图片相对链接补充完整
                all_pic = url + all_pic
            absolute_pic = re.findall(pattern, str(all_pic))
            if len(absolute_pic) != 0:
                piclist.append(absolute_pic[0])
                picstr = picstr + absolute_pic[0] + ' '

        # 提取网页所有脚本
        scriptlist = []
        scriptstr = ' '
        for script in soup.find_all('script'):
            javascript = script.get('src')
            if javascript != None and len(javascript) != 0 and (javascript[0] != 'h' or javascript[1] != 't' or javascript[2] != 't' or javascript[3] != 'p') and javascript[0] == '/':   # 将网页的脚本相对链接补充完整:
                javascript = url + javascript
            absolute_javascript = re.findall(pattern, str(javascript))
            if len(absolute_javascript) != 0:
                scriptlist.append(absolute_javascript[0])
                scriptstr = picstr + absolute_javascript[0] + ' '



        # 提取页面关键词
        keyword = ''
        for meta in soup.find_all('meta'):
            if meta.get('name') == "keywords":
                keyword = meta.get('content')

        # 提取网页所有文字内容
        html_text = soup.get_text()

        # 提取页面标题
        if soup.title is not None:
            html_title = soup.title.string
        else:
            html_title = None

        # print(soup.title)
        # print(soup.title.name)
        # print(soup.title.parent.name)
        # print(soup.p)
        # print(soup.p['class'])
        # print(soup.a)

    except urllib.error.URLError as e:
        access_flag = 0  # 网页不可访问
        linklist = None
        linkstr = None
        piclist = None
        picstr = None
        scriptlist = None
        scriptstr = None
        keyword = None
        html_text = None
        html_title = None


    return linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title,access_flag


# url = 'http://douban.com'  # 要爬取的url页面
# linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title,access_flag = htmlinfo_extraction(url)
# print(scriptlist)
