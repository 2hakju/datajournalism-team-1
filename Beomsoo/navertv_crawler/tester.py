#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from datetime import datetime

with open(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_crawler\nahonja_2017.json", 'r', encoding = 'utf-8') as file:
    data = pd.read_json(file, orient = 'records')

data_date = data.dropna(how = 'any')


def converter(d) :
    r = d.replace(',','')
    if r != '':
        return int(r)
    else :
        return 0



data_date['reply_count'] = data_date['reply_count'].apply(lambda d : converter(d))
data_date['play_count'] = data_date['play_count'].apply(lambda d : converter(d))
data_date['heart_count'] = data_date['heart_count'].apply(lambda d : converter(d))
# except ValueError:
#     f

data_reflist = []
for date,rows in data_date.groupby("date"):
    data_ref = {}
    data_ref['date'] = date
    data_ref['heart_count_sum'] = rows.heart_count.sum()
    data_ref['play_count_sum'] = rows.play_count.sum()
    data_ref['reply_count_sum'] = rows.reply_count.sum()
    data_reflist.append(data_ref)
    
print(data_reflist)

