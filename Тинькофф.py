#!/usr/bin/env python
# coding: utf-8

# In[91]:


import requests

df = pd.read_json (r'https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/tinkoff_hh.json', lines = True)

for i in range(len(df)):
    if i%2 == 1:
        df['index'][i] = (i-1)/2
        df.drop(i-1, inplace=True)
        
def ch(x):
    if ch != 'не указан':
        a = x.replace('\xa0','')[2:9]
        b = ''
        for i in list(a):
            if i.isdigit():
                b = b + str(i)
    if b != '':
        return int(b)
    

df['средняя з/п'] = list(map(ch,list(df.income)))
df_1 = df.groupby(['vacancy'])['средняя з/п'].value_counts()
df_1.head()


# In[ ]:




