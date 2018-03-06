file = open('train.conll')
content = file.read()
f = content.split('\n\n')
d = str(f[0])
g = d.split('\n')
len1 = 0
len2 = 0
word = []
tag = []
for i in range(len(f)):
    d = str(f[i])
    g = d.split('\n')
    len1 +=1
    for item in g:
        item = item.split('\t')
        len2 +=1
        if item[0] not in word:
           word.append(item[0])
        if item[-1] not in tag:
            tag.append(item[-1])
print(word)
print(len(word))
for i in range(len(tag)):
    if tag[i] == '':
        tag.remove('')

print(tag)
print(len(tag))
print(len1)
print(len2)
print(len(f))


"""
for i in f:
    print(i)
"""
file.close
