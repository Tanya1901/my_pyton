#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/new_year_film.csv"
f = pd.read_csv(url)
ls = f['ranking'].values
ls = str(ls)
ls = ls.replace('[','')
ls = ls.replace(']','')
ls = ls.replace('\n','')
ls = ls.replace(',','.')
ls = ls.replace("'",'')
ls = ls.split()

l = list(map(float, ls))
print(sum(l)/len(l))


# In[ ]:




