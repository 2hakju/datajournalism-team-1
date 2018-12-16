#%%
date = '등록213.3243.324 작업'
date = date.replace('등록', '')
print(date)
import time
import json
data_list = ["1,2,3"]

time.sleep(10)
try : 
    1+2 
except KeyboardInterrupt :
    print('크롤링이 완료됐습니다.')
    with open('nahonja_2015.json', 'w', encoding="utf-8") as make_file:
        json.dump(data_list, make_file, ensure_ascii=False, indent = '\t')

#%%
from datetime import datetime
print(datetime(2018,12,7))