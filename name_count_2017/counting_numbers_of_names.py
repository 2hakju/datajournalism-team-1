from konlpy.tag import Kkma, Komoran
import random
from collections import Counter

kkma = Kkma()
tagger = Komoran()

with open('_text1.txt', 'r', encoding='utf-8') as f:
        lines1 = f.read().splitlines()
with open('_text2.txt', 'r', encoding='utf-8') as f:
        lines2 = f.read().splitlines()
with open('_text3.txt', 'r', encoding='utf-8') as f:
        lines3 = f.read().splitlines()
with open('_text4.txt', 'r', encoding='utf-8') as f:
        lines4 = f.read().splitlines()

lines = lines1 + lines2 + lines3 + lines4
'''
for i in range(len(lines)):
    print(i)
    print(lines[i])
'''
print(len(lines))

#name_count1 (quarter1)
morph_list = []
for line in lines1:
    try:
        morph_list += tagger.pos(line)

    except:
        pass

print(len(morph_list))
name_list = []
for word, tag in morph_list:
    if tag in ['NNP']:
        name_list.append(word)

name_count = Counter(name_list)
print(name_count.most_common(100))

with open('muhan_name_count1.txt', 'w', encoding='utf-8') as f:
    for name, count in name_count.most_common():
        data = str(name) + ': ' + str(count) + '\n'
        f.write(data)
        
#name_count2 
morph_list = []
for line in lines1:
    try:
        morph_list += tagger.pos(line)

    except:
        pass

print(len(morph_list))
name_list = []
for word, tag in morph_list:
    if tag in ['NNP']:
        name_list.append(word)

name_count = Counter(name_list)
print(name_count.most_common(100))

with open('_name_count2.txt', 'w', encoding='utf-8') as f:
    for name, count in name_count.most_common():
        data = str(name) + ': ' + str(count) + '\n'
        f.write(data)

        
#name_count3
morph_list = []
for line in lines1:
    try:
        morph_list += tagger.pos(line)

    except:
        pass

print(len(morph_list))
name_list = []
for word, tag in morph_list:
    if tag in ['NNP']:
        name_list.append(word)

name_count = Counter(name_list)
print(name_count.most_common(100))

with open('_name_count3.txt', 'w', encoding='utf-8') as f:
    for name, count in name_count.most_common():
        data = str(name) + ': ' + str(count) + '\n'
        f.write(data)

#name_count4
morph_list = []
for line in lines1:
    try:
        morph_list += tagger.pos(line)

    except:
        pass

print(len(morph_list))
name_list = []
for word, tag in morph_list:
    if tag in ['NNP']:
        name_list.append(word)

name_count = Counter(name_list)
print(name_count.most_common(100))

with open('_name_count4.txt', 'w', encoding='utf-8') as f:
    for name, count in name_count.most_common():
        data = str(name) + ': ' + str(count) + '\n'
        f.write(data)


#name_count_all
morph_list = []
for line in lines:
    try:
        morph_list += tagger.pos(line)

    except:
        pass

print(len(morph_list))
name_list = []
for word, tag in morph_list:
    if tag in ['NNP']:
        name_list.append(word)

name_count = Counter(name_list)
print(name_count.most_common(100))

with open('_name_count_all.txt', 'w', encoding='utf-8') as f:
    for name, count in name_count.most_common():
        data = str(name) + ': ' + str(count) + '\n'
        f.write(data)    
