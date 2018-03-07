# fin1 = open("train.conll",encoding = 'utf-8')
# fin2 = open("test.conll",encoding = 'utf-8')
# content1 = fin1.read()
# content2 = fin2.read()
# f = content1.split('\n\n')
# d = content2.split('\n\n')
# f1 = f[0]
# f2 = d[0]
# print(f1)
# print(f2)
# for i in range(len(f2)):
#     f2[i].decode('utf-8')+" "+f1[-1].decode('utf-8')



with open("test.conll", encoding='utf-8') as f:
    for line in f:
        if line.strip():
            print('{}\t{}'.format(line.strip(), 'MYPOSTAG'))
        else:
            print()