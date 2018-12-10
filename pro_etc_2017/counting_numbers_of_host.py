
textfile = '{}2016_text{}qt.txt'
countfile = '{}2016_host_count{}.txt'
pro1 = 'muhan'
pro2
pro3
pro4
pro5
pro6



with open(textfile.format(pro, '1'), 'r', encoding='utf-8') as f:
        lines1 = f.read().splitlines()
with open(textfile.format(pro, '2'), 'r', encoding='utf-8') as f:
        lines2 = f.read().splitlines()
with open(textfile.format(pro, '3'), 'r', encoding='utf-8') as f:
        lines3 = f.read().splitlines()
with open(textfile.format(pro, '4'), 'r', encoding='utf-8') as f:
        lines4 = f.read().splitlines()

lines = lines1 + lines2 + lines3 + lines4


broadcast = ['김성주', '김구라', '신봉선', '이윤석', '김현철', '유영석']

#1
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in lines1:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(pro, '1'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)

        
#2
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in lines2:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(pro, '2'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)
    

#3
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in lines3:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(pro, '3'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)



#4
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in lines4:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(pro, '4'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)



#all
broad_dict = dict()

for i in broadcast:
    count = 0
    for line in lines:
        count = count + line.count(i)
        broad_dict[i] = count

print(broad_dict)


with open(countfile.format(pro, '_all'), 'w', encoding='utf-8') as f:
    for i in broadcast:
        data = i + str(': ') + str(broad_dict[i]) + '\n'
        f.write(data)















