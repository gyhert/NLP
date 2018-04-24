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
cx = {}
cy = {}
for i in tag:
    cx[i] = 0
    cy[i] = 0
    pi[i] = pi[i] * 1.0 / len1
    for j in tag:
        if A[i][j] == 0:
            cx[i] += 1
            A[i][j] = 0.3
    for j in word:
        if B[i][j] == 0:
           cy[i] += 1
           B[i][j] = 0.3
for i in tag:
    pi[i] = pi[i] * 1.0 / len1
    for j in tag:
        A[i][j] = A[i][j]*1.0/(fre[i] + cx[i])
    for j in word:
        B[i][j] = B[i][j]*1.0/(fre[i] + cy[i])
"""test set/initial/smooth/viterbi/backtracking """

file_test = open('test.conll', encoding='utf-8')
content = file_test.read()
f3 = content.split('\n\n')
for i in range(len(f3)):
    d = str(f3[i])
    g = d.split('\n')
    len_sent = len(g)
    dp = [{} for i in range(len_sent)]
    pre2 = [{} for i in range(len_sent)]
    for k in tag:
        for j in range(len_sent):
            dp[j][k] = 0
            pre2[j][k] = ""
    word0 = g[0].split('\t')
    for c in tag:
        if word0[0] in B[c]:
            dp[0][c] = pi[c]*(B[c][word0[0]])*1500
        else:
            dp[0][c] = pi[c]*0.3*1000/(cy[c] + fre[c])
    for i in range(len_sent):
        word1 = g[i].split('\t')
        for j in tag:
            for k in tag:
                tt = 0
                if word1[0] in B[j]:
                    tt = B[j][word1[0]]*1500
                else:
                    tt = 0.3*1000 / (cy[j] + fre[j])
                if dp[i][j] < dp[i-1][k]*A[k][j]*tt:
                   dp[i][j] = dp[i-1][k]*A[k][j]*tt
                   pre2[i][j] = k

    MAX = ""
    res = {}
    for j in tag:
        if MAX == "" or dp[len_sent-1][j] > dp[len_sent-1][MAX] :
            MAX = j
    if dp[len_sent-1][MAX] == 0:
        continue
    i = len_sent - 1
    while i >= 0:
        res[i] = MAX
        MAX = pre2[i][MAX]
        i -= 1
    for i in range(0, len_sent):
        print('{}\t{}'.format(g[i], res[i]))
    print()

file_dev.close
file.close
file_test.close