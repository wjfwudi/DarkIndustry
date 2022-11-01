import jieba.analyse


def tf_idf(text):
    text = text

    # jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
    # sentence 为待提取的文本
    # topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20




    # withWeight 为是否一并返回关键词权重值，默认值为 False
    # allowPOS 仅包括指定词性的词，默认值为空，即不筛选

    keywords = jieba.analyse.extract_tags(text, topK=10, withWeight=False, allowPOS=())
    return keywords

# text = '澳门六合彩499377.com，澳门六合彩资料，澳门六合彩官网，澳门六合彩开奖结果，澳门六合彩开奖直播，澳门六合彩论坛，澳门六合彩图库，台湾六合彩，新加坡六合彩'
# keywords  = tf_idf(text)
# print(keywords)