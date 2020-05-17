#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"

football = pd.read_csv(url)
football.head()


# In[2]:


small_football = football[football.columns[1:8]].head(25)
small_football


# In[12]:


s = small_football['Club'].value_counts()
s.count()


# In[14]:


small_football['Club'].min()


# In[24]:



s = small_football['Position'].value_counts(normalize=True)
s.loc[s>0.1]


# In[25]:



s = small_football['Position'].value_counts(normalize=True)
s.loc[s<0.01]


# In[32]:


s = small_football['Wage'].value_counts(bins=4)
s


# In[ ]:





# In[30]:


small_football.loc[(small_football['Wage'] > s.index[3].left) & 
                   (small_football['Wage'] <= s.index[3].right)]


# In[49]:


s = football['FKAccuracy'].value_counts(bins=5)
s.index[0]


# In[61]:


s = football['FKAccuracy'].value_counts()
s.index[0]


# In[73]:


s = football[football.Nationality =="Spain"].Wage.value_counts(bins=4)
round(len(football.loc[(football['Wage'] > s.index[0].left) & 
                   (football['Wage'] <= s.index[0].right)])/len(football)*100)


# In[80]:


s = football[football.Club == "Manchester United"].Nationality.unique()
len(s)


# In[102]:


s = football[(football.Nationality == "Brazil") & (football.Club == "Juventus")].Name.unique()
s


# In[109]:


s = football[football.Age>35].Club.value_counts()
s.index[0]


# In[119]:


s = football[football.Nationality == "Argentina"].Age.value_counts(bins=4)
s[[3]]


# In[124]:


s = football[(football.Nationality == "Spain") & (football.Age == 21)].Name.count()
round(s/len(football[football.Nationality == "Spain"])*100,2)

