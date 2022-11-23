import opencc
import jieba

def text_transform(text):
    # 删除空格、制表符等特殊字符
    test_new = text.replace("\n","")
    # test_new = test_new.replace(" ","")
    # test_new = test_new.replace("\r","")
    # test_new = test_new.replace("\t","")
    cc = opencc.OpenCC('t2s')
    test_new = cc.convert(test_new)   # 繁字体转化为简体字
    test_new = test_new.lower()       # 大写字母转化为小写
    return test_new


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

# 去除utf8不可见字符
def remove_upprintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())
