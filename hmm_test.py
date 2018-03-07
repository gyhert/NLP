file = open('train.conll')
file_dev = open('dev.conll')
content1 = file.read()
f = content1.split('\n\n')

len1 = 0
len2 = 0
"""initial parameter"""
word = []
word_fre = {}
tag = []
fre = {}
pi = {}
A = {}
B = {}
dp =[]
pre = []
zz = {}
"""get words and tags"""
"""sentence"""
for i in range(len(f)):
    d = str(f[i])
    g = d.split('\n')
    len1 +=1
    for j in range(len(g)):
        len2 +=1
        item = g[j].split('\t')
        if item[0] not in word:
           word.append(item[0])
        if item[-1] == '':
            print(item)
        if item[-1] not in tag:
            tag.append(item[-1])
"""dev"""
content2 = file_dev.read()
f2 = content2.split('\n\n')
for i in range(len(f2)):
    d = str(f2[i])
    g = d.split('\n')
    len1 +=1
    for j in range(len(g)):
        len2 +=1
        item = g[j].split('\t')
        if item[0] not in word:
           word.append(item[0])
for i in range(len(tag)):
    if tag[i] == '':
        tag.remove('')
print(len1)
print(len2)
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
        if post[-1] in tag:
            fre[post[-1]] +=1
        if j > 0 and post[-1] in tag:
           A[prev[-1]][post[-1]] += 1
        if post[-1] in tag:
           B[post[-1]][post[0]] += 1
           L +=1
for i in range(len(f2)):
    d = str(f2[i])
    g = d.split('\n')
    line_first = g[0].split('\t')
    if line_first[-1] in pi:
        pi[line_first[-1]] += 1
    for j in range(len(g)):
        post = g[j].split('\t')
        prev = g[j-1].split('\t')
        if post[-1] in tag:
            fre[post[-1]] +=1
        if j > 0 and post[-1] in tag:
           A[prev[-1]][post[-1]] += 1
        if post[-1] in tag:
           B[post[-1]][post[0]] += 1
           L +=1
print(len(B))
cx = {}
cy = {}
for i in tag:
    cx[i] = 0
    cy[i] = 0
    pi[i] = pi[i] * 1.0 / len1
    for j in tag:
        if A[i][j] == 0:
            cx[i] += 1
            A[i][j] = 0.5
    for j in word:
        if B[i][j] == 0:
           cy[i] += 1
           B[i][j] = 0.5
for i in tag:
    pi[i] = pi[i] * 1.0 / len1
    for j in tag:
        A[i][j] = A[i][j]*1.0/(fre[i] + cx[i])
    for j in word:
        B[i][j] = B[i][j]*1.0/(fre[i] + cy[i])
print(len(A))
print(len(B))
print(pi)
"""test set """
"""
with open("test.conll", encoding='utf-8') as f:
    for line in f:
        if line.strip():
            print('{}\t{}'.format(line.strip(), 'MYPOSTAG'))
        else:
            print()
"""







