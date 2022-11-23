import urllib
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import ssl
import jieba
import text_process
import os



def htmltext_extraction(URL):
    global i
    i = i + 1
    if URL.startswith('http'):
        url = URL
    else:
        url = 'http://' + URL
    print(i)
    
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'Cookie': 'AEC=AakniGPStgBkE78oYqyNUWGnKvt78i97hfV89Q9M1Qfga3WpkcVoaONb16Q; OTZ=6738220_24_24__24_; DV=Q-AFApj3WM0gYIMZotJe81q5eO2OQBjiKlD-42UvvwIAAAA; NID=511=VZCPeWmnoWY__R9euAw8DYLgdEl82NMiD-xnUIUO0yDS1OoLOjp4xydWKDf9Bs0yBs9dHPk3Aa3cho_t923bwGxW47Sv8bga2QhZsKpbPHmGJjYqJDltvsFFRQIYI2dZ4ivRTMvaOg5QhpTBLuFDKMlgKQV15GUOE4J85jmTjG2v8SuL-90_VhQVZvLMpN6kjMarKhbnIA; 1P_JAR=2022-10-24-07'
    }  # 头部信息
    ssl._create_default_https_context = ssl._create_unverified_context  # 关闭https的认证
    try:
        request = urllib.request.Request(url,headers=header)
        reponse = urllib.request.urlopen(request).read()

        soup = BeautifulSoup(reponse, 'html.parser')

        # 提取网页所有文字内容
        html_text = soup.get_text()

        #去除不可见字符
        html_text = text_process.remove_upprintable_chars(html_text)
        
        # 大小写和繁体
        html_text = text_process.text_transform(html_text)

        

        # 分词
        sentence_seged = jieba.cut(html_text.strip())

        outstr = ''
        for word in sentence_seged:
            if word not in stopwords:
                if word != '\t' and word != '\xa0' and word != '\u2800' and word != '\u3000':
                    outstr = outstr + word + " "
                    #outstr.append(word)
        out = open("1.txt", "a",encoding="utf-8")
        # print(outstr)
        out.write(outstr+'\n')
        out.close()
        

    except Exception as e:
        pass


    
# 加载停用词
stopwords = [line.strip() for line in open(r'C:\Users\wjf\Documents\Tencent Files\942356504\FileRecv\stop_words.txt', 'r', encoding='utf-8')]




path = r'D:\python\writeup\DarkIndustry\dataset\datasets'
file_list = os.listdir(path)


for name in file_list:
    if name.startswith('task'):
        print(name)
        i = 0
        for line in open(path + '/' + name,encoding='utf-8'):   
            htmltext_extraction(line)
            




        

