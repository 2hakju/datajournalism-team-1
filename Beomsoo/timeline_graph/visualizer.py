#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import datetime 
get_ipython().run_line_magic('matplotlib', 'inline')

def opener(url):
    with open(url, 'r', encoding = 'utf-8') as file:
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

    data_reflist = []
    for date,rows in data_date.groupby("date"):
        data_ref = {}
        data_ref['date'] = date
        data_ref['heart_count_mean'] = rows.heart_count.mean()
        data_ref['play_count_mean'] = rows.play_count.mean()
        data_ref['reply_count_mean'] = rows.reply_count.mean()
        data_reflist.append(data_ref)

    pand = pd.DataFrame.from_records(data_reflist)
    return pand


#%%
#open files
mudo = opener(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_crawler\mudo_2017.json")
mudo = mudo.iloc[1:]   #무도는 2009년 데이터가 하나 포함되어 있어서 그 데이터 제거해줌.
nahonja = opener(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_crawler\nahonja_2017.json")
bokga = opener(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_crawler\bokga_2017.json")
radio = opener(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_crawler\radio_2017.json")
data_list = [(mudo,'mudo'), (nahonja,'nahonja'), (bokga,'bokga'), (radio,'radio')]

#%%
def visualizer(data_list, category):

    #2017/1/1 ~ 2018/1/1 까지의 날짜 list 생성
    start_day = datetime.datetime(2017,1,1)   
    one_day = datetime.timedelta(days = 1)    
    end_day = datetime.datetime(2017,12,28) # 2017 연예대상 시상식 날짜 기준

    date_list = []
    
    while start_day < end_day:
        date_list.append(start_day)
        start_day = start_day + one_day
        
    plt.figure(num = None, figsize = (18,9))
    
    x1 = data_list[0][0]['date']
    y1 = data_list[0][0][category]
    x2 = data_list[1][0]['date']
    y2 = data_list[1][0][category]
    x3 = data_list[2][0]['date']
    y3 = data_list[2][0][category]
    x4 = data_list[3][0]['date']
    y4 = data_list[3][0][category]
    plt.plot(x1, y1, label = data_list[0][1], color = 'r')
    plt.plot(x2, y2, label = data_list[1][1], color = 'y')
    plt.plot(x3, y3, label = data_list[2][1], color = 'g')
    plt.plot(x4, y4, label = data_list[3][1], color = 'b')
    plt.legend()
    plt.title(category)
    plt.xticks(rotation=90)
    plt.savefig(category)
    return
    plt.show()

visualizer(data_list, 'heart_count_mean')
visualizer(data_list, 'reply_count_mean')
visualizer(data_list, 'play_count_mean')