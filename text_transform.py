import opencc

def text_transform(text):
    # 删除空格、制表符等特殊字符
    test_new = text.replace("\n","")
    test_new = test_new.replace(" ","")
    test_new = test_new.replace("\r","")
    test_new = test_new.replace("\t","")
    cc = opencc.OpenCC('t2s')
    test_new = cc.convert(test_new)   # 繁字体转化为简体字
    test_new = test_new.lower()       # 大写字母转化为小写
    return test_new


# s1 = "採菊東籬下，悠然見南山.Buifl   hauglis  jifao;nafuiohHO    UHFOIEHUI"
# s2 = text_transform(s1)
# print(s2)