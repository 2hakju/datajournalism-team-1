#%%
import json
import pandas as pd

# json 그냥 읽어오기
with open(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_crawler\nahonja_2017.json", 'r', encoding = 'utf-8') as file:
    pands = pd.read_json(file, orient = 'records')

reply_list = pands.reply_list
reply_list

#%%
# tagging 하기
from konlpy.tag import Komoran
tagger = Komoran()
tagged_sentences = [tagger.pos(sent[0]) for sent in reply_list]
tagged_sentences

#%%
unique_nouns = set()
for sent in tagged_sentences:    
    for word, tag in sent:
        if tag in ['NNP', 'NNG']:
            unique_nouns.add(word)

unique_nouns = list(unique_nouns)
# unique_nouns
noun_index = {noun: i for i, noun in enumerate(unique_nouns)}

import numpy as np
occurs = np.zeros([len(tagged_sentences), len(unique_nouns)])
np.shape(occurs)

for i, sent in enumerate(tagged_sentences):
    for word, tag in sent:
        if tag in ['NNP', 'NNG']:
            index = noun_index[word]  # 명사가 있으면, 그 명사의 인덱스를 index에 저정
            occurs[i][index] = 1  # 문장 i의 index 자리에 1을 채워 넣는다.

#%%
### 공존 단어 행렬 계산

co_occurs = occurs.T.dot(occurs)

co_occurs[0]

### 연관 단어의 network graph 그리기

import networkx as nx
graph = nx.Graph()

for i in range(len(unique_nouns)):
    for j in range(i + 1, len(unique_nouns)):
        if co_occurs[i][j] > 1:
            graph.add_edge(unique_nouns[i], unique_nouns[j])

%matplotlib inline
import matplotlib.pyplot as plt
# import matplotlib.font_manager as fm
# fp1 = fm.FontProperties(fname = "")

plt.figure(figsize=(15, 15))
layout = nx.spring_layout(graph, k=.5)
nx.draw(graph, pos=layout, with_labels=True,
        font_size=20, font_family="‪C:\Windows\Fonts\oldbath.ttf",
        alpha=0.3, node_size=3000)
plt.show()