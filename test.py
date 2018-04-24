#f = open('train.conll')
#o = open('dev.conll', 'w')
#for line in f:
#   line2 = str(line.strip('\r\n')) + '\n'
#  o.write(line2)
file = open('test.conll')
file_dev = open('submission3.txt')
content1 = file.read()
f = content1.split('\n\n')
content2 = file_dev.read()
f2 = content2.split('\n\n')
a = 0
b = 0
print(len(f))
print(len(f2))
for i in range(len(f)):
    d1 = f[i].split('\n')
    g1 = d1[0]
    d2 = f2[i].split('\n')
    g2 = d2[0].split('\t')
    g1 = d1[0].split('\t')
    print(g2)


