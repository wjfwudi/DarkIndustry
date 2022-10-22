
import pymysql
# from spider import htmlinfo_extraction


# url = 'https://jd.com/'  # 菜鸟教程搜索页面
# linklist,linkstr,piclist,picstr,scriptlist,scriptstr,keyword,html_text,html_title,access_flag = htmlinfo_extraction(url)


# 将解析的网页数据保存在数据库中
#Filename,Formula,SpaceGroup,SpaceGroupName  形参
def ConnectMysql(URL,LINKSTR,PICSTR,SCRIPTSTR,KEYWORD,HTML_TITLE,HTML_TEXT,ACCESS_FLAG):
    #1.连接数据库 连接名称，账户 密码 端口 数据库名称
    conn = pymysql.Connection(host = 'localhost',user = 'root', password = 'Lq309557!' , port = 3306 ,database ='darkindustry')
    #2.生成游标对象
    cursor = conn.cursor()
    #3.sql插入赋值语句
    # %s占位符
    sql = "INSERT INTO dark_web_info (url,linkstr,picstr,scriptstr,keyword,html_title,html_text,access_flag) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    #4.执行SQL语句
    #sql必须放入

    try:
        # 执行sql语句
        # [filename,formula,spacegroup,spacegroupname]为占位符中所需要的数据 可以根据自己的需求传参传进来
        cursor.execute(sql, [URL, LINKSTR, PICSTR, SCRIPTSTR, KEYWORD, HTML_TEXT, HTML_TITLE, ACCESS_FLAG])
        # 提交到数据库执行
        conn.commit()
    except:
        # 如果发生错误则回滚
        # conn.rollback()
        pass

    conn.close()



# ConnectMysql(url,linkstr,picstr,scriptstr,keyword,html_title,html_text,access_flag)

