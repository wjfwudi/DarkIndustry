path1 = 'dataset/datacon2021_darkindustry/domains.txt'

# 读取制定路径下 数据集文件给出的url
def ReadFile(path):
    s = []
    f = open(path,'r')

    for lines in f:
        ls = lines.strip("\n")
        s.append(ls)
    f.close()
    return s

s = ReadFile(path1)
print(s)