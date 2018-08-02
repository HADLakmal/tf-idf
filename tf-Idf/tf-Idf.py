import re
import collections
import nltk
from nltk.corpus import stopwords
import math


with open("stopwords.txt",encoding = "ISO-8859-1") as f:
    data = f.read()
stop = data.split('\n')
def tokenize(data):
    tokens = re.findall(r"\w*", data, re.UNICODE)
    tokenArray = []
    for r in tokens:
        word = str(r).lower().replace(' ','').replace('\n','').replace('\xa0','')
        if(word not in stop):
            continue
        elif(word.isdecimal()):
            continue
        condition = True
        for char in word:
            if(char.isalpha() is False):
                condition = False
                break
        if condition:
            tokenArray.append(word)
    dic = collections.OrderedDict()
    tokenArray = sorted(list(tokenArray))
    for team in [ele for ind, ele in enumerate(tokenArray,1) if ele not in tokenArray[ind:]]:
        dic[team] = tokenArray.count(team)
    #print(tockenDic)

    return dic



index = 34

with open("document1.txt",encoding = "ISO-8859-1") as f:
    data = f.read()
dic1 = tokenize(data)
# tokens = re.findall("\s*(\w*)\s*", datas, re.UNICODE)
with open("document2.txt",encoding = "ISO-8859-1") as f:
    data2 = f.read()
dic2 = tokenize(data2)
with open("document3.txt",encoding = "ISO-8859-1") as f:
    data3 = f.read()
dic3 = tokenize(data3)


print("..................Documnet 1 data...............")
print("Document vacabullary size : ", len(dic1))
print(list(dic1)[index], " = tf value : ", 1 + math.log10(dic1[list(dic1)[index]]))
N = 1
if(list(dic1)[index] in list(dic2)):
    N+=1
    if (list(dic1)[index] in list(dic3)):
        N+=1
print(list(dic1)[index], " = idf value : ", math.log10(3/N),'\n')


print("..................Documnet 2 data...............")
print("Document vacabullary size : ", len(dic2))
print(list(dic2)[index], " = tf value : ", 1 + math.log10(dic2[list(dic2)[index]]))
N = 1
if(list(dic2)[index] in list(dic1)):
    N+=1
    if (list(dic2)[index] in list(dic3)):
        N+=1
print(list(dic2)[index], " = idf value : ", math.log10(3/N),'\n')


print("..................Documnet 3 data...............")
print("Document vacabullary size : ", len(dic3))
print(list(dic3)[index], " = tf value : ", 1 + math.log10(dic3[list(dic3)[index]]))
N = 1
if(list(dic3)[index] in list(dic1)):
    N+=1
    if (list(dic3)[index] in list(dic2)):
        N+=1
print(list(dic3)[index], " = idf value : ", math.log10(3/N),'\n')