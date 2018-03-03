import re
import string

twitter_file = 'twitter.txt'
def read_file(file):
    return [l.rstrip() for l in open(file)]

def ex12(file):
    lines = read_file(file)
    list = []
    r = re.compile('^^[A-Z].*(#[a-zA-Z0-9_]+|@[a-zA-Z0-9_]+)$')
    j = r.findall(lines[i])
    if len(j) != 0:
             list.append(lines[i])
    return list
ex12(twitter_file)