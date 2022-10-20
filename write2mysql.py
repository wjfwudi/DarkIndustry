
import pymysql

ID = 1
URL = "www.baidu.com"
Page_title_and_keyword = "你好"
Pure_text_content = " 今天十个好日子！" \
                    "呵呵 "

# 将解析的网页数据保存在数据库中
#Filename,Formula,SpaceGroup,SpaceGroupName  形参
def ConnectMysql(ID,URL,Page_title_and_keyword,Pure_text_content):
    #1.连接数据库 连接名称，账户 密码 端口 数据库名称
    conn = pymysql.Connection(host = 'localhost',user = 'root', password = 'Lq309557!' ,port = 3306 ,database ='darkindustry')
    #2.生成游标对象
    cursor = conn.cursor()
    #3.sql插入赋值语句
    # %s占位符
    sql = "INSERT INTO dark_web_info (id,url,page_title_and_keyword,pure_text_content) VALUES (%s,%s,%s,%s)"
    #4.执行SQL语句
    #sql必须放入
    #[filename,formula,spacegroup,spacegroupname]为占位符中所需要的数据 可以根据自己的需求传参传进来
    cursor.execute(sql,[ID,URL,Page_title_and_keyword,Pure_text_content])
    #5.提交数据库事务
    conn.commit()
    conn.close()

ConnectMysql(ID,URL,Page_title_and_keyword,Pure_text_content)

