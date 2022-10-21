path1 = 'dataset/datacon2021_darkindustry/domains.txt'
path2 = 'dataset/datasets/darkindustry20200801_4afd29926db588548fe384dc70000d16ffd6e52b/task_20200801.txt'

# 读取制定路径下 数据集文件给出的url
def ReadFile(path):
    s = []
    f = open(path,'r')
    str1 = "http://"
    for lines in f:
        ls = lines.strip("\n")
        if ls[0] != 'h' or ls[1] != 't' or ls[2] != 't' or ls[3] != 'p':
            ls = str1 + ls
            s.append(ls)
        else:
            s.append(ls)
    f.close()
    return s

# s = ReadFile(path1)
# print(s[1:20])