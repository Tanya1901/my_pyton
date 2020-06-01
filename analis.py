#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/vkontakte_group_01_2016-08-01_2020-03-15.csv")
df.head()


# In[14]:


from datetime import date
from datetime import datetime, timedelta

def d(data):
    n1 = datetime.strptime(data, '%d.%m.%Y')
    n2 = n1.year
    return n2
crit = df[df['Критерий'] == 'views']
crit['Дата_2'] = crit.apply(lambda x: d(x.Дата), axis = 1)
y16 = round(crit[crit['Дата_2'] == 2016]["Значение"].mean())
y17 = round(crit[crit['Дата_2'] == 2017]["Значение"].mean())
y18 = round(crit[crit['Дата_2'] == 2018]["Значение"].mean())
y19 = round(crit[crit['Дата_2'] == 2019]["Значение"].mean())
y20 = round(crit[crit['Дата_2'] == 2020]["Значение"].mean())
crit1=[y16, y17, y18, y19, y20]
data=["2016","2017","2018","2019","2020"]
plt.plot(data, crit1)


# In[16]:


visit = df[df['Критерий'] == 'visitors']
visit['Дата_2'] = visit.apply(lambda x: d(x.Дата), axis = 1)
y16 = round(visit[visit['Дата_2'] == 2016]["Значение"].mean())
y17 = round(visit[visit['Дата_2'] == 2017]["Значение"].mean())
y18 = round(visit[visit['Дата_2'] == 2018]["Значение"].mean())
y19 = round(visit[visit['Дата_2'] == 2019]["Значение"].mean())
y20 = round(visit[visit['Дата_2'] == 2020]["Значение"].mean())
visit1=[y16, y17, y18, y19, y20]
data=["2016","2017","2018","2019","2020"]
plt.plot(data, visit1)


# In[17]:


r1 = df[(df['Критерий'] == 'reach')]['Значение'].sum()
r2 = df[(df['Критерий'] == 'reach_subscribers')]['Значение'].sum()
r = r1 - r2
import matplotlib.pyplot as pltt
lbl = ["Подписаны","Не подписаны"]
val = [r2,r]
fig, ax = pltt.subplots()
ax.pie(val, labels=lbl)
pltt.show()


# In[18]:


m=df[(df["Парам. №1"] == "М")]["Значение"].sum()
w=df[(df["Парам. №1"] == "Ж")]["Значение"].sum()
lbl_1 = ["Мужчины","Женщины"]
val_1 = [m,w]
fig_1, ax_1 = pltt.subplots()
ax_1.pie(val_1, labels=lbl_1)
pltt.show()


# In[19]:


k = (df[(df["Парам. №1"] == "1-18")]["Значение"].sum()) + (df[(df["Парам. №2"] == "1-18")]["Значение"].sum())
t = (df[(df["Парам. №1"] == "18-21")]["Значение"].sum()) + (df[(df["Парам. №2"] == "18-21")]["Значение"].sum())
y = (df[(df["Парам. №1"] == "21-24")]["Значение"].sum()) + (df[(df["Парам. №2"]== "21-24")]["Значение"].sum())
y_1 = (df[(df["Парам. №1"] == "24-27")]["Значение"].sum()) + (df[(df["Парам. №2"] =="24-27")]["Значение"].sum())
y_2 = (df[(df["Парам. №1"] == "27-30")]["Значение"].sum()) + (df[(df["Парам. №2"] == "27-30")]["Значение"].sum())
o = (df[(df["Парам. №1"] == "30-35")]["Значение"].sum()) + (df[(df["Парам. №2"] == "30-35")]["Значение"].sum())
o_1 = (df[(df["Парам. №1"] == "35-45")]["Значение"].sum()) + (df[(df["Парам. №2"] == "35-45")]["Значение"].sum())
o_2 = (df[(df["Парам. №1"] == "45+")]["Значение"].sum()) + (df[(df["Парам. №2"] == "45+")]["Значение"].sum())
lbl_2 = ["1-18","18-21","21-24","24-27","27-30","30-35","35-45","45+"]
val_2 = [k, t, y, y_1, y_2, o, o_1, o_2]
fig_2, ax_2 = pltt.subplots()
ax_2.pie(val_2, labels=lbl_2)
pltt.show()


# In[20]:


c = df[df["Критерий"] == "countries"]["Парам. №1"].unique()
ln = len(df[df["Критерий"] == "countries"]["Парам. №1"].unique())

l = []
for i in range(ln):
    x = df[(df["Критерий"] == "countries") & (df["Парам. №1"] == c[i])]["Значение"].sum()
    l.append(x)
srt = sorted(l, reverse = True)
sum(srt[3::])
el = (list(c)[:3])
srt[:3]


fig_3, ax_3 = pltt.subplots()
ax_3.pie([22367, 994, 506,sum(srt[3::])], labels = ['Россия', 'Украина', 'Беларусь','Другие'])
pltt.show()


# In[22]:


like=df[(df['Критерий']=="feedback")&(df['Парам. №1']=='Нравится')]
like['Дата2'] = like.apply(lambda x: d(x.Дата), axis=1)
y16 = round(like[like["Дата2"] == 2016]["Значение"].mean())
y17 = round(like[like["Дата2"] == 2017]["Значение"].mean())
y18 = round(like[like["Дата2"] == 2018]["Значение"].mean())
y19 = round(like[like["Дата2"] == 2019]["Значение"].mean())
y20 = round(like[like["Дата2"] == 2020]["Значение"].mean())
like1 = [y16, y17, y18, y19, y20]
plt.plot(data,like1)


# In[23]:


com = df[(df['Критерий'] == "feedback") & (df['Парам. №1'] == 'Комментарии')]
com['Дата2'] = com.apply(lambda x: d(x.Дата), axis=1)
y16 = round(com[com["Дата2"] == 2016]["Значение"].mean())
y17 = round(com[com["Дата2"] == 2017]["Значение"].mean())
y18 = round(com[com["Дата2"] == 2018]["Значение"].mean())
y19 = round(com[com["Дата2"] == 2019]["Значение"].mean())
y20 = round(com[com["Дата2"] == 2020]["Значение"].mean())
com1 = [y16, y17, y18, y19, y20]
plt.plot(data, com1)


# In[24]:


repost = df[(df['Критерий'] == "feedback") & (df['Парам. №1'] == 'Рассказали друзьям')]
repost['Дата2'] = repost.apply(lambda x: d(x.Дата), axis=1)
y16 = round(repost[repost["Дата2"] == 2016]["Значение"].mean())
y17 = round(repost[repost["Дата2"] == 2017]["Значение"].mean())
y18 = round(repost[repost["Дата2"] == 2018]["Значение"].mean())
y19 = round(repost[repost["Дата2"] == 2019]["Значение"].mean())
y20 = round(repost[repost["Дата2"] == 2020]["Значение"].mean())
repost1 = [y16, y17, y18, y19, y20]
plt.plot(data, repost1)


# In[25]:


upom = df[(df['Критерий'] == "feedback") & (df['Парам. №1'] == 'Упоминания')]
upom['Дата2'] = upom.apply(lambda x: d(x.Дата), axis=1)
u = round(upom[upom["Дата2"] == 2019]["Значение"].mean())
upom1 = [0,0,0,u,0]
plt.plot(data, upom1)


# In[ ]:


По получившемуся анализу видно, что в 2020 году отклик 
аудитории пошел на спад, поэтому, несмотря на то, что
основная аудитория младше 30, которой больше половины, и на то, что
большая часть пользователей в России, скоро эта группа может
стать пустой. То есть не стоит в нее вкладывать ресурсы.  

