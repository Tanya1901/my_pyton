#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

url = 'https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv'

df = pd.read_csv(url)
df.head()


# In[8]:



grouped_df = df.groupby(['Club']).sum()
grouped_df


# In[10]:


grouped_df = df.groupby(['Club'])['Wage'].sum().sort_values(ascending=False)
grouped_df.head(5)


# In[21]:


d = df.groupby(['Position'])[['Wage','Value']].mean().sort_values(['Wage'], ascending=False).head(1)
d


# In[31]:


d = df.groupby("Club")['Wage'].agg(['mean', 'median'])
d


# In[51]:


dd = d.loc[d["mean"] == d["median"]].sort_values(['mean'], ascending=False)
dd


# In[54]:


dd.max()


# In[50]:


dd.index[0]


# In[62]:


df.groupby(['Club'])[['Wage']]
df.loc[df['Club'] == 'Chelsea'][['Wage']].sum()


# In[63]:


df.loc[(df['Nationality'] == 'Argentina') & (df['Age'] == 20)][['Wage']].max()


# In[64]:


df.loc[(df['Nationality'] == 'Argentina') & (df['Age'] == 30)][['Wage']].max()


# In[65]:


df.loc[(df['Nationality'] == 'Argentina') & (df['Age'] == 30)][['Wage']].min()


# In[75]:


a = df.loc[(df['Club'] == 'FC Barcelona') & (df['Nationality'] == 'Argentina')][['Strength']].max()
b = df.loc[(df['Club'] == 'FC Barcelona') & (df['Nationality'] == 'Argentina')][['Balance']].max()
print(str(a["Strength"])+';'+str(b['Balance']))


# In[ ]:




