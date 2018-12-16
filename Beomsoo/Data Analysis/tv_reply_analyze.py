#%%
import pandas as pd


def text_a(path):
    with open(path, 'r', encoding = 'utf-8') as file:
        data = pd.read_json(file, orient = 'records')
    return data[['date','reply_list']]

replies = text_a(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\mudo_2015.json")
text_list = []
for a in replies.reply_list :
    for text in a:
        text_list.append(text)
text_list

from konlpy.tag import Komoran
tagger = Komoran()
tagged_sentences = [tagger.pos(sent) for sent in text_list]
print(tagged_sentences)

noun_list = []
for sent in tagged_sentences:    
    for word, tag in sent:
        if tag in ['NNP', 'NNG']:
            noun_list.append(word)

from collections import Counter
noun_counts = Counter(noun_list)
print(noun_counts.most_common())




# path_list = [r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\mudo_2015.json",
#              r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\bokga_2015.json",
#              r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\nahonja_2015.json",
#              r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\radio_2015.json"
#              ]
# for a in path_list:
