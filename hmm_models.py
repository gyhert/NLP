file = open('train.conll')
content = file.read()
f = content.split('\n\n')
"""
d = str(f[0])
g = d.split('\n')
j = str(g[0])
h = j.split('\t')
print(g)
print(h)
"""
len1 = 0
len2 = 0

"""initial parameter"""

#all words
word = []
#word_fre
word_fre = {}
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
    """
    line_first = (g[0]).split('\t')
    if line_first[0] in pi:
        pi[line_first[0]] +=1
    else:
        pi[line_first[0]] = 1
    """
    for j in range(len(g)):
        len2 +=1
        item = g[j].split('\t')
        if item[0] not in word:
           word.append(item[0])
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
"""initial A B """
for i in tag:
    pi[i] = 0
    fre[i] = 0
    A[i] = {}
    B[i] = {}
    for j in tag:
        A[i][j] = 0
    for j in word:
        B[i][j] = 0
L = 0
for i in range(len(f)):
    d = str(f[i])
    g = d.split('\n')
    line_first = g[0].split('\t')
    if line_first[-1] in pi:
        pi[line_first[-1]] += 1
    for j in range(len(g)):
        post = g[j].split('\t')
        prev = g[j-1].split('\t')
        if j > 0:
           A[prev[-1]][post[-1]] += 1
        if post[-1] in tag:
           B[post[-1]][post[0]] += 1
print(L)

cx = {}
cy = {}
for i in tag:
    cx[i] = 0
    cy[i] = 0
    pi[i] = pi[i] * 1.0 /len1
    for j in tag:
        if A[i][j] == 0:
            cx[i] += 1
            A[i][j] = 0.5
    for j in word:
        if B[i][j] == 0:
           cy[i] += 1
           B[i][j] = 0.5

print(pi)







"""
for i in f:
    print(i)
"""
file.close
