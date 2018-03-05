file = open('dev.conll')
content = file.read()
f = content.split('\n\n')

f = str(f[0])
print(f)
print(len(f))



"""
for i in f:
    print(i)
"""
file.close
