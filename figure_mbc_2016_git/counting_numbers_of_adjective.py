from konlpy.tag import Kkma, Komoran
import random
from collections import Counter

kkma = Kkma()
tagger = Komoran()

textfile = '{}2016_text{}qt.txt'
countfile = '{}2016_adj_count{}.txt'


pro1 = 'jaesuk'
pro2 = 'junha'
pro3 = 'kura'
pro4 = 'sungju'


def read_textfile(name, num):
    with open(textfile.format(name, str(num)), 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
    return lines



#name_count1 (quarter1)
def get_morph_list(lines):
    morph_list = []
    for line in lines:
        try:
            morph_list += tagger.pos(line)

        except:
            pass
    print(len(morph_list))
    return morph_list

def get_noun_count(morphlist):
    name_list = []
    for word, tag in morphlist:
        if tag in ['VA']:
            name_list.append(word)

    name_count = Counter(name_list)
    name_count.most_common(100)
    return name_count

def get_countdict(pro):
    broad_dict = dict()
    for i in broadcast:
        count = 0
        for line in pro:
            count += line.count(i)
            broad_dict[i] = count
    print(broad_dict)
    return broad_dict

def make_countfile(x, st, count):
    with open(countfile.format(x, st), 'w', encoding='utf-8') as f:
        for name, count in count.most_common():
            data = str(name) + ': ' + str(count) + '\n'
            f.write(data)
    return True
        
pro1_lines1 = read_textfile(pro1, 1)
pro1_lines2 = read_textfile(pro1, 2)
pro1_lines3 = read_textfile(pro1, 3)
pro1_lines4 = read_textfile(pro1, 4)
pro1_lines = pro1_lines1 + pro1_lines2 + pro1_lines3 + pro1_lines4

pro2_lines1 = read_textfile(pro2, 1)
pro2_lines2 = read_textfile(pro2, 2)
pro2_lines3 = read_textfile(pro2, 3)
pro2_lines4 = read_textfile(pro2, 4)
pro2_lines = pro2_lines1 + pro2_lines2 + pro2_lines3 + pro2_lines4

pro3_lines1 = read_textfile(pro3, 1)
pro3_lines2 = read_textfile(pro3, 2)
pro3_lines3 = read_textfile(pro3, 3)
pro3_lines4 = read_textfile(pro3, 4)
pro3_lines = pro3_lines1 + pro3_lines2 + pro3_lines3 + pro3_lines4

pro4_lines1 = read_textfile(pro4, 1)
pro4_lines2 = read_textfile(pro4, 2)
pro4_lines3 = read_textfile(pro4, 3)
pro4_lines4 = read_textfile(pro4, 4)
pro4_lines = pro4_lines1 + pro4_lines2 + pro4_lines3 + pro4_lines4



#jaesuk
morph_1 = get_morph_list(pro1_lines1)
morph_2 = get_morph_list(pro1_lines2)
morph_3 = get_morph_list(pro1_lines3)
morph_4 = get_morph_list(pro1_lines4)
morph_all = get_morph_list(pro1_lines)

countdict_1 = get_noun_count(morph_1)
countdict_2 = get_noun_count(morph_2)
countdict_3 = get_noun_count(morph_3)
countdict_4 = get_noun_count(morph_4)
countdict_all = get_noun_count(morph_all)

make_countfile(pro1, '1', countdict_1)
make_countfile(pro1, '2', countdict_2)
make_countfile(pro1, '3', countdict_3)
make_countfile(pro1, '4', countdict_4)
make_countfile(pro1, '_all', countdict_all)

#pro2
morph_1 = get_morph_list(pro2_lines1)
morph_2 = get_morph_list(pro2_lines2)
morph_3 = get_morph_list(pro2_lines3)
morph_4 = get_morph_list(pro2_lines4)
morph_all = get_morph_list(pro2_lines)

countdict_1 = get_noun_count(morph_1)
countdict_2 = get_noun_count(morph_2)
countdict_3 = get_noun_count(morph_3)
countdict_4 = get_noun_count(morph_4)
countdict_all = get_noun_count(morph_all)

make_countfile(pro2, '1', countdict_1)
make_countfile(pro2, '2', countdict_2)
make_countfile(pro2, '3', countdict_3)
make_countfile(pro2, '4', countdict_4)
make_countfile(pro2, '_all', countdict_all)


#pro3
morph_1 = get_morph_list(pro3_lines1)
morph_2 = get_morph_list(pro3_lines2)
morph_3 = get_morph_list(pro3_lines3)
morph_4 = get_morph_list(pro3_lines4)
morph_all = get_morph_list(pro3_lines)

countdict_1 = get_noun_count(morph_1)
countdict_2 = get_noun_count(morph_2)
countdict_3 = get_noun_count(morph_3)
countdict_4 = get_noun_count(morph_4)
countdict_all = get_noun_count(morph_all)

make_countfile(pro3, '1', countdict_1)
make_countfile(pro3, '2', countdict_2)
make_countfile(pro3, '3', countdict_3)
make_countfile(pro3, '4', countdict_4)
make_countfile(pro3, '_all', countdict_all)

#pro4
morph_1 = get_morph_list(pro4_lines1)
morph_2 = get_morph_list(pro4_lines2)
morph_3 = get_morph_list(pro4_lines3)
morph_4 = get_morph_list(pro4_lines4)
morph_all = get_morph_list(pro4_lines)

countdict_1 = get_noun_count(morph_1)
countdict_2 = get_noun_count(morph_2)
countdict_3 = get_noun_count(morph_3)
countdict_4 = get_noun_count(morph_4)
countdict_all = get_noun_count(morph_all)

make_countfile(pro4, '1', countdict_1)
make_countfile(pro4, '2', countdict_2)
make_countfile(pro4, '3', countdict_3)
make_countfile(pro4, '4', countdict_4)
make_countfile(pro4, '_all', countdict_all)
