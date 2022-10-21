from spider import htmlinfo_extraction
from write2mysql import ConnectMysql
from Readfiles import ReadFile

path1 = 'dataset/datacon2021_darkindustry/domains.txt'
path2 = 'dataset/datasets/darkindustry20200801_4afd29926db588548fe384dc70000d16ffd6e52b/task_20200801.txt'

s = ReadFile(path1)
for html in s:
    linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title = htmlinfo_extraction(html)
    print(html_title)

# linklist, linkstr, piclist, picstr, scriptlist, scriptstr, keyword, html_text, html_title = htmlinfo_extraction(s[2])
# print(html_title)


# url = 'http://www.baidu.com/'  # 菜鸟教程搜索页面
# linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title = htmlinfo_extraction(url)
# print(keyword)