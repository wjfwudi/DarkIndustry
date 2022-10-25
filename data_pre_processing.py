from spider import htmlinfo_extraction
from write2mysql import ConnectMysql
from Readfiles import ReadFile

path0 = 'dataset/datacon2021_darkindustry/domains.txt'
path1 = 'dataset/datasets/darkindustry20200801_4afd29926db588548fe384dc70000d16ffd6e52b/task_20200801.txt'
path2 = 'dataset/datasets/darkindustry20200802_13ed8f4bba39cb176b56b002abfad62a42c619c2/task_20200802.txt'
path3 = 'dataset/datasets/darkindustry20200803_ffede6e9950b9dc0a86cd8f4d5f7fb1daeae3b4a/task_20200803.txt'
path4 = 'dataset/datasets/darkindustry20200804_f044a119861514c9afeef921429df5858b99ed36/task_20200804.txt'
path5 = 'dataset/datasets/darkindustry20200805_9c2b735502680c26de57a5433c25e88eb6f6bb14/task_20200805.txt'
path6 = 'dataset/datasets/darkindustry20200806_ab5ce18836e961dfe38750f1e8b2b65487410a00/task_20200806.txt'
path7 = 'dataset/datasets/darkindustry20200807_63892a39300298c2dc922913bb28aa23af443367/task_20200807.txt'
path8 = 'dataset/datasets/darkindustry20200808_ffede6e9950b9dc0a86cd8f4d5f7fb1daeae3b4a/task_20200808.txt'
path9 = 'dataset/datasets/darkindustry20200809_13ed8f4bba39cb176b56b002abfad62a42c619c2/task_20200809.txt'
path10 = 'dataset/datasets/darkindustry202008010_ab5ce18836e961dfe38750f1e8b2b65487410a00/task_20200810.txt'
path11 = 'dataset/datasets/darkindustry202008011_bc6b8a0d2b9349eeb0deb238187c9e314e92a9d0/task_20200811.txt'
path12 = 'dataset/datasets/darkindustry202008014_e93ce96d9f058ffb0ffe075822ceb5fd858edb54/task_20200812_20200814.txt'


# s = ReadFile(path2)
# for html in s:
#     print("爬取" + html + "网页的数据...")
#     linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title,access_flag = htmlinfo_extraction(html)
#     ConnectMysql(html,linkstr,picstr,scriptstr,keyword,html_title,html_text,access_flag)
#     print(html + "网页的数据爬取成功，并已保存在数据库中")

# linklist, linkstr, piclist, picstr, scriptlist, scriptstr, keyword, html_text, html_title = htmlinfo_extraction(s[2])
# print(html_title)


url = 'http://17173.chat'  # 菜鸟教程搜索页面
linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title,access_flag = htmlinfo_extraction(url)
print(keyword)
