from spider import *
from text_transform import text_transform
from LDA import *
from write2mysql import ConnectMysql
from seed_keywords import seed_keywords
# for i in range(97):
#     print(i)

# ls = "hdt88.cn"
# str1 = "http://"
# if ls[0] != 'h' or ls[1] != 't' or ls[2] != 't' or ls[3] != 'p':
#     ls = str1 + ls
# print(ls)

url = 'http://douban.com'  # 要爬取的url页面
linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title,access_flag = htmlinfo_extraction(url)
# print(html_text)
new_html_text  = text_transform(html_text)


# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist(r'C:\Users\Lu\PycharmProjects\DarkIndustry\dataset\LDA_datasets\stop_words.txt')  # 这里加载停用词的路径
    outstr = []
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t' and word != '\xa0' and word != '\u2800' and word != '\u3000':
                # outstr = outstr + word + " "
                outstr.append(word)
    return outstr

print(keyword)
print(html_title)

new_keyword = seg_sentence(keyword)
new_tile = seg_sentence(html_title)
print(new_keyword)
print(new_tile)
print(seed_keywords)
s1 = seg_sentence(new_html_text)
print(s1)
# print(s1)
title_and_keyword = new_keyword + new_tile
print(title_and_keyword)


title_and_keyword = ['douban','日韩','勇士']
for word in title_and_keyword:
    for k,v in seed_keywords.items():
        if word in v:
            print(k)
