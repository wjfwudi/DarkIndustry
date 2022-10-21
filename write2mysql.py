
import pymysql
# from spider import htmlinfo_extraction


# url = 'https://www.douban.com/'  # 菜鸟教程搜索页面
# linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title = htmlinfo_extraction(url)


# 将解析的网页数据保存在数据库中
#Filename,Formula,SpaceGroup,SpaceGroupName  形参
def ConnectMysql(ID,URL,LINKSTR,PICSTR,SCRIPTSTR,KEYWORD,HTML_TITLE,HTML_TEXT):
    #1.连接数据库 连接名称，账户 密码 端口 数据库名称
    conn = pymysql.Connection(host = 'localhost',user = 'root', password = 'Lq309557!' , port = 3306 ,database ='darkindustry')
    #2.生成游标对象
    cursor = conn.cursor()
    #3.sql插入赋值语句
    # %s占位符
    sql = "INSERT INTO dark_web_info (id,url,linkstr,picstr,scriptstr,keyword,html_title,html_text) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    #4.执行SQL语句
    #sql必须放入
    #[filename,formula,spacegroup,spacegroupname]为占位符中所需要的数据 可以根据自己的需求传参传进来
    cursor.execute(sql,[ID,URL,LINKSTR,PICSTR,SCRIPTSTR,KEYWORD,HTML_TEXT,HTML_TITLE])
    #5.提交数据库事务
    conn.commit()
    conn.close()



# ConnectMysql(id,url,linkstr,picstr,scriptstr,keyword,html_title,html_text)

