#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pymorphy2
from itertools import groupby
import numpy

a = []
a1 = []
a2 = []
b = []
c = []


url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data_stat/yandex-stat-q.csv"

df = pd.read_csv(url)
df.head()
morph = pymorphy2.MorphAnalyzer()

d = df['Поисковая фраза'].tolist()
l = len(d)

for x in range(l):
    a.extend(d[x].split())

    for i in a:
        if len(i) > 1:
            if i[0] == '“' and i[-1] == '”':
                a1.append(str(i[1:-2]))
            elif i[0] == '“' or i[0] == '”' or i[0] == '"' or i[0] == ',' or i[0] == '«' or i[0] == ','or i[0] == '?':
                a1.append(str(i[1::]))
            elif i[-1] == ',' or i[-1] == '”' or i[-1] == '“' or i[-1] == '?' or i[-1] == '»' or i[-1] == '.':
                a1.append(str(i[::-2]))
            elif i[-3:-1] == '...':
                a1.append(str(i[::-4]))
            elif i[::2] == '...':
                a1.append(str(i[3::]))
            else:
                a1.extend(i.split('.'))
                a1.extend(i.split('/'))
    for i in a1:
        if len(i) > 1:
            if i[0] == '“' and i[-1] == '”':
                a2.append(str(i[1:-2]))
            elif i[0] == '“' or i[0] == '”' or i[0] == '"' or i[0] == ',' or i[0] == '«' or i[0] == ',':
                a2.append(str(i[1::]))
            elif i[-1] == ',' or i[-1] == '”' or i[-1] == '“' or i[-1] == '?' or i[-1] == '»' or i[-1] == '.':
                a2.append(str(i[::-2]))
            elif i[-3:-1] == '...':
                a2.append(str(i[::-4]))
            elif i[::2] == '...':
                a2.append(str(i[3::]))
            else:
                a2.extend(i.split('.'))
                a2.extend(i.split('/'))      

    for j in a2:
        if j != '':
            b.append(morph.parse(j)[0].normal_form)
            x += 1
    a = []
    a1 = []
    a2 = []
    
new_b = [el for el, _ in groupby(b)]
for y in new_b:
    c.append(str(b.count(y)))
             
col_width = max(len(word) for row in [new_b,c] for word in row) + 2 
for row in numpy.transpose([new_b,c]):
    print ("".join(word.ljust(col_width) for word in row))

