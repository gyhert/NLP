# all word
ww = []
# all pos
pos = []

# pos fre
fre = {}
# pre pro
pre = {}
# state transform matrix
A = {}

# 观测矩阵

B = {}

#dp 概率
dp = []

#路径记录

pre = []
zz = {}

fin = open('dev.conll')
text = fin.readline()
print(text)
temp = text.strip('\t')
print(temp[0])
n = len(temp)
for i in range(0,n-1):
    word = temp[i]




