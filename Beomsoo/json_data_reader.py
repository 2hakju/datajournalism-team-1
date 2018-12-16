#%%
import json
import pandas as pd
from datetime import datetime

# json 그냥 읽어오기
json_data = []
with open(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\mudo_2015.json", 'r', encoding = 'utf-8') as file:
    pands = pd.read_json(file, orient = 'records')

pands
# pands['date'][1] == datetime(2015,1,3)
# radio_2017 = json_data[0]
# print(json_data)

# pandas로 읽어오기
# nahonja_data = pd.read_json(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\navertv_crawler\navertv_nahonja_2017.json", orient='records', encoding = 'utf-8')
# mudo_data = pd.read_json(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\navertv_crawler\navertv_mudo_2017.json", orient = 'records')
# radio_data = pd.read_json(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\navertv_crawler\radio_2017.json", orient='records', encoding = 'utf-8')
# print(mudo_data)

# with open (r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Bemsoo\navertv_crawler\mudo_2017.json") as f:
#     data = json.load(f, encoding = 'utf-8')

# mudo_2017 = pd.DataFrame(data)
# print(mudo_2017)