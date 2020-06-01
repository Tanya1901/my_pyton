#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import requests  

res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

res.text[:230]
cr = res.json()
df = pd.read_csv('https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/it_new.csv')

def conv(sal):
    if sal=="₽":
        k=1
    elif sal=="$":
        k=currencies['Valute']['USD']['Value']
    elif sal=="€":
        k=currencies['Valute']['EUR']['Value']
    elif sal=="lev":
        k=currencies['Valute']['BGN']['Value']
    elif sal=="Kč":
        k=currencies['Valute']['CZK']['Value']
    elif sal=="zł":
        k=currencies['Valute']['PLN']['Value']
    elif sal=="Ft":
        k=currencies['Valute']['HUF']['Value']
    return k

df['З/п в рублях']=df['col']*df['curenc'].apply(conv)
df.head(10)


# In[ ]:




