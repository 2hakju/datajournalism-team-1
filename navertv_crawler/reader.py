
import json
import ast

json_data = []
with open(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\navertv_crawler\navertv_mudo_2017.json", encoding = 'utf-8') as file:
    data = file.readlines()
    for d in data:
        json_data.append(json.loads(d))
mudo_2017 = json_data[0]
