
textfile = '{}2015_text{}qt.txt'
countfile = '{}2015_host_count{}.txt'
mbc = 'mbc'

pro1 = 'nahonja'
pro2 = 'mylittletv'
pro3 = 'sectiontv'
pro4 = 'showmusic'
pro5 = 'wemarried'
pro6 = 'iamsinger'
pro7 = 'bokmyen'
pro8 = 'muhan'
pro9 = 'radiostar'
pro10 = 'realman'


#balchick
with open(textfile.format(pro1, '1'), 'r', encoding='utf-8') as f:
        pro1_lines1 = f.read().splitlines()
with open(textfile.format(pro1, '2'), 'r', encoding='utf-8') as f:
        pro1_lines2 = f.read().splitlines()
with open(textfile.format(pro1, '3'), 'r', encoding='utf-8') as f:
        pro1_lines3 = f.read().splitlines()
with open(textfile.format(pro1, '4'), 'r', encoding='utf-8') as f:
        pro1_lines4 = f.read().splitlines()

pro1_lines = pro1_lines1 + pro1_lines2 + pro1_lines3 + pro1_lines4

#bokmyen
with open(textfile.format(pro2, '1'), 'r', encoding='utf-8') as f:
        pro2_lines1 = f.read().splitlines()
with open(textfile.format(pro2, '2'), 'r', encoding='utf-8') as f:
        pro2_lines2 = f.read().splitlines()
with open(textfile.format(pro2, '3'), 'r', encoding='utf-8') as f:
        pro2_lines3 = f.read().splitlines()
with open(textfile.format(pro2, '4'), 'r', encoding='utf-8') as f:
        pro2_lines4 = f.read().splitlines()

pro2_lines = pro2_lines1 + pro2_lines2 + pro2_lines3 + pro2_lines4

#muhan
with open(textfile.format(pro3, '1'), 'r', encoding='utf-8') as f:
        pro3_lines1 = f.read().splitlines()
with open(textfile.format(pro3, '2'), 'r', encoding='utf-8') as f:
        pro3_lines2 = f.read().splitlines()
with open(textfile.format(pro3, '3'), 'r', encoding='utf-8') as f:
        pro3_lines3 = f.read().splitlines()
with open(textfile.format(pro3, '4'), 'r', encoding='utf-8') as f:
        pro3_lines4 = f.read().splitlines()

pro3_lines = pro3_lines1 + pro3_lines2 + pro3_lines3 + pro3_lines4

#nahonja
with open(textfile.format(pro4, '1'), 'r', encoding='utf-8') as f:
        pro4_lines1 = f.read().splitlines()
with open(textfile.format(pro4, '2'), 'r', encoding='utf-8') as f:
        pro4_lines2 = f.read().splitlines()
with open(textfile.format(pro4, '3'), 'r', encoding='utf-8') as f:
        pro4_lines3 = f.read().splitlines()
with open(textfile.format(pro4, '4'), 'r', encoding='utf-8') as f:
        pro4_lines4 = f.read().splitlines()

pro4_lines = pro4_lines1 + pro4_lines2 + pro4_lines3 + pro4_lines4

#ojimagic #1qt x

with open(textfile.format(pro5, '1'), 'r', encoding='utf-8') as f:
        pro5_lines1 = f.read().splitlines()
with open(textfile.format(pro5, '2'), 'r', encoding='utf-8') as f:
        pro5_lines2 = f.read().splitlines()
with open(textfile.format(pro5, '3'), 'r', encoding='utf-8') as f:
        pro5_lines3 = f.read().splitlines()
with open(textfile.format(pro5, '4'), 'r', encoding='utf-8') as f:
        pro5_lines4 = f.read().splitlines()

pro5_lines = pro5_lines1 + pro5_lines2 + pro5_lines3 + pro5_lines4

#radiostar
with open(textfile.format(pro6, '1'), 'r', encoding='utf-8') as f:
        pro6_lines1 = f.read().splitlines()
with open(textfile.format(pro6, '2'), 'r', encoding='utf-8') as f:
        pro6_lines2 = f.read().splitlines()
'''
with open(textfile.format(pro6, '3'), 'r', encoding='utf-8') as f:
        pro6_lines3 = f.read().splitlines()
with open(textfile.format(pro6, '4'), 'r', encoding='utf-8') as f:
        pro6_lines4 = f.read().splitlines()
'''
pro6_lines = pro6_lines1 + pro6_lines2 

#sectiontv
with open(textfile.format(pro7, '1'), 'r', encoding='utf-8') as f:
        pro7_lines1 = f.read().splitlines()
with open(textfile.format(pro7, '2'), 'r', encoding='utf-8') as f:
        pro7_lines2 = f.read().splitlines()
with open(textfile.format(pro7, '3'), 'r', encoding='utf-8') as f:
        pro7_lines3 = f.read().splitlines()
with open(textfile.format(pro7, '4'), 'r', encoding='utf-8') as f:
        pro7_lines4 = f.read().splitlines()

pro7_lines = pro7_lines1 + pro7_lines2 + pro7_lines3 + pro7_lines4

#semobang2017 #1qt x

with open(textfile.format(pro8, '1'), 'r', encoding='utf-8') as f:
        pro8_lines1 = f.read().splitlines()
with open(textfile.format(pro8, '2'), 'r', encoding='utf-8') as f:
        pro8_lines2 = f.read().splitlines()
with open(textfile.format(pro8, '3'), 'r', encoding='utf-8') as f:
        pro8_lines3 = f.read().splitlines()
with open(textfile.format(pro8, '4'), 'r', encoding='utf-8') as f:
        pro8_lines4 = f.read().splitlines()

pro8_lines =  pro8_lines1 + pro8_lines2 + pro8_lines3 + pro8_lines4

#showmusic
with open(textfile.format(pro9, '1'), 'r', encoding='utf-8') as f:
        pro9_lines1 = f.read().splitlines()
with open(textfile.format(pro9, '2'), 'r', encoding='utf-8') as f:
        pro9_lines2 = f.read().splitlines()
with open(textfile.format(pro9, '3'), 'r', encoding='utf-8') as f:
        pro9_lines3 = f.read().splitlines()
with open(textfile.format(pro9, '4'), 'r', encoding='utf-8') as f:
        pro9_lines4 = f.read().splitlines()

pro9_lines = pro9_lines1 + pro9_lines2 + pro9_lines3 + pro9_lines4

#voguemom 1,2qt x
with open(textfile.format(pro10, '1'), 'r', encoding='utf-8') as f:
        pro10_lines1 = f.read().splitlines()
with open(textfile.format(pro10, '2'), 'r', encoding='utf-8') as f:
        pro10_lines2 = f.read().splitlines()
with open(textfile.format(pro10, '3'), 'r', encoding='utf-8') as f:
        pro10_lines3 = f.read().splitlines()
with open(textfile.format(pro10, '4'), 'r', encoding='utf-8') as f:
        pro10_lines4 = f.read().splitlines()

pro10_lines = pro10_lines1 + pro10_lines2 + pro10_lines3 + pro10_lines4





pro_1 = pro1_lines1 + pro2_lines1 + pro3_lines1 + pro4_lines1 + pro5_lines1 + pro6_lines1 + pro7_lines1 + pro8_lines1 + pro9_lines1 + pro10_lines1 
pro_2 = pro1_lines2 + pro2_lines2 + pro3_lines2 + pro4_lines2+ pro5_lines2 + pro6_lines2 + pro7_lines2 + pro8_lines2 + pro9_lines2 + pro10_lines2 
pro_3 = pro1_lines3 + pro2_lines3 + pro3_lines3 + pro4_lines3 + pro5_lines3  + pro7_lines3 + pro8_lines3 + pro9_lines3 + pro10_lines3 
pro_4 = pro1_lines4 + pro2_lines4 + pro3_lines4 + pro4_lines4 + pro5_lines4  + pro7_lines4 + pro8_lines4 + pro9_lines4 + pro10_lines4 

pro_all = pro1_lines + pro2_lines + pro3_lines + pro4_lines + pro5_lines + pro6_lines + pro7_lines + pro8_lines + pro9_lines + pro10_lines 


broadcast = ['전현무', '김광규', '육중완', '김용건', '이태곤', '김동완', '김영철', '강민혁', '황석정', '김구라', '정준하', '윤박', '은지원', '정형돈',
 			'윤종신', '김국진', '규현', '초아', '백종원', '이은결', '김영만', '황재근', '차홍', '이말년', '김동현', '박명수', '유재석', '하하', '황광희',
			'소이현', '임지연', '민호', '김소현', '지코', '예리', '엔', '김민재', '김새론', '김성주', '신봉선', '이윤석', '김현철', '유영석']
#1
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in pro_1:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(mbc, '1'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)

        

#2
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in pro_2:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(mbc, '2'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)



#3
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in pro_3:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(mbc, '3'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)


#4
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in pro_4:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(mbc, '4'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)



#1
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in pro_all:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(mbc, '_all'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)





