from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.impute import SimpleImputer
import jieba
import numpy as np
#字典特征抽取
def dictvec():
    dict = DictVectorizer(sparse=False)
    #字典转换成二维数组
    data = dict.fit_transform([{'city':'yc','temperature':10}
                           ,{'city':'wh','temperature':100}
                            ,{'city':'gd','temperature':1000}
                               ,{'city':'yc','temperature':10}])
    print(data)
    #特征名称
    print(dict.get_feature_names())
    # 转换成字典

    print(dict.inverse_transform(data))
    return None

# 统计文本特征（英语）
def countvec():
    cv = CountVectorizer()
    data = cv.fit_transform(["qqqq wwww eeee rrrr aaaa aaaa"
                                ,"wwww tttt yyyy aaaa"
                                ,"eeee pppp uuuu yyyy tttt"
                             ,"rrrr eeee wwww tttt"])
    print(data)
    print(data.toarray())   # 每句话中每个单词出现的次数
    #统计特征的种类（包含的所有单词）
    print(cv.get_feature_names())
    return None

#是有jieba分词
def cutword():
    con1 = jieba.cut("很多被吸引来的买家都是一次性的，他们在这次消费之后就再也没有购买，针对这些用户的促销活动并没有给店铺带来未来销售的增加。")
    con2 = jieba.cut("通过对这些潜在的忠诚客户进行精细化营销，商家可以大大降低促销成本，提高投资回报率。")
    con3 = jieba.cut("换句话说，你需要预测这些新买家在未来六个月内再次在同一个商家购买商品的概率。我们给出一个包含约20万用户的数据集进行训练，另一个规模相近的数据集进行测试。与其他比赛类似，你可以提取任何特征，然后用其他工具进行训练。你只需要提交预测结果进行评估。")
    # 转换成列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)
    # 转换成字符串
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)

    return c1,c2,c3

#提取汉字文本的特征
def hanzivec():
    c1,c2,c3 = cutword()
    print(c1,c2,c3)

    cv = CountVectorizer()
    data = cv.fit_transform([c1,c2,c3])
    print(data)
    print(data.toarray())
    # 统计特征的种类
    print(cv.get_feature_names())
    return None

#
def tfidfvec():
    c1, c2, c3 = cutword()
    print(c1, c2, c3)

    tf = TfidfVectorizer()
    data = tf.fit_transform([c1, c2, c3])
    print(data)
    print(data.toarray())
    # 统计特征的种类
    print(tf.get_feature_names())
    return None

#归一化处理
def mm():
    mm = MinMaxScaler(feature_range=(0,1))#指定区间范围
    data = mm.fit_transform([[11,12,13,14],[50,60,70,80],[55,66,77,88]])
    print(data)

# 标准化处理
def stander():
    std = StandardScaler()
    data = std.fit_transform([[11,12,13,14],[50,60,70,80],[55,66,77,88]])
    print(data)
    return None

#https://scikit-learn.org/stable/modules/impute.html#impute
# 最新版0.22版本sklearn，imputer不在preprocessing里了，
# 而是在sklearn.impute里，除了SimpleImputer外，还增加了KNNImputer。
# 另外还有IterativeImputer用法
#缺失值填充
def simpleimputer():
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')

    # imp.fit([[1, 2], [np.nan, 3], [7, 6]])
    X = [[np.nan, 2], [6, np.nan], [7, 6]]
    # print(imp.transform(X))

    data = imp.fit_transform(X)
    print(data)

    return None

if __name__ == "__main__":
    # dictvec()
    # print("-----------------------------------------------")
    # countvec()
    # print("-----------------------------------------------")
    # hanzivec()
    # print("-----------------------------------------------")
    tfidfvec()
    # print("-----------------------------------------------")
    # mm()
    # print("-----------------------------------------------")
    # stander()
    # print("-----------------------------------------------")
    # simpleimputer()
