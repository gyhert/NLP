file = open('train.conll')
content = file.read()
f = content.split('\n\n')
d = str(f[0])
g = d.split('\n')
j = str(g[0])
h = j.split('\t')
print(g)
print(h)
len1 = 0
len2 = 0

"""initial parameter"""

#all words
word = []
#all tag
tag = []
#每个词出现的概率
fre = {}
#先验概率矩阵
pi = {}
#状态转移概率矩阵
A = {}
#观测概率矩阵
B = {}
# dp概率
dp =[]
#路径记录
pre = []
zz = {}
"""get words and tags"""
"""sentence"""
for i in range(len(f)):
    d = str(f[i])
    g = d.split('\n')
    len1 +=1
    """word"""
    line_first = (g[0]).split('\t')
    if line_first[0] in pi:
        pi[line_first[0]] +=1
    else:
        pi[line_first[0]] = 1
    for j in range(len(g)):
        item = g[j].split('\t')
        if item[0] not in word:
           word.append(item[0])
           if item[0] in fre:
               fre[item[0]] +=1
           else:
               fre[item[0]] = 1
        if item[-1] == '':
            print(item)

        if item[-1] not in tag:
            tag.append(item[-1])
print(len(word))
for i in range(len(tag)):
    if tag[i] == '':
        tag.remove('')


print(tag)
print(len(tag))
print(len1)
print(len(f))
for i in tag:
    pi[i] = 0
    fre[i] = 0
    A[i] = {}
    B[i] = {}
    for j in tag:
        A[i][j] = 0
    for j in word:
        B[i][j] = 0


"""
for i in f:
    print(i)
"""
file.close
