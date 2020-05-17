#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

url = "https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/football.csv"

football = pd.read_csv(url)
football.head()


# In[11]:


age = football["Age"]
round(age.mean())


# In[12]:


com = football["Composure"]
com.count()


# In[27]:


sp = football["ShortPassing"]
round(sp.std(),2)


# In[28]:


sum1 = football["Wage"]
sum1.sum()


# In[29]:


v = football["Value"]
min(v)


# In[30]:


round(football[football.Wage>football.Wage.mean()].SprintSpeed.mean(),2)


# In[31]:


round(football[football.Wage<football.Wage.mean()].SprintSpeed.mean(),2)


# In[32]:


football[football.Wage==football.Wage.max()].Position


# In[33]:


football[football.Nationality=="Brazil"].Penalties.sum()


# In[34]:


round(football[football.HeadingAccuracy>50].Age.mean(),2)


# In[39]:


football[(football.Composure>0.9*football.Composure.max()) & (football.Reactions>0.9*football.Reactions.max())].Age.min()


# In[40]:


round(football[football.Age==football.Age.max()].Reactions.mean()-football[football.Age==football.Age.min()].Reactions.mean(),2)


# In[41]:


football[football.Value>football.Value.mean()].Nationality.max()


# In[42]:


round(football[(football.Position=="GK") & (football.GKReflexes==football.GKReflexes.max())].Wage.mean()/football[(football.Position=="GK") & (football.GKHandling==football.GKHandling.max())].Wage.mean(),2)


# In[43]:


round(football[football.Aggression==football.Aggression.max()].ShotPower.mean()/football[football.Aggression==football.Aggression.min()].ShotPower.mean(),2)

