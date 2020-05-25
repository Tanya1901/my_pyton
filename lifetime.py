#!/usr/bin/env python
# coding: utf-8

# In[18]:


import datetime
from datetime import datetime, timedelta

date_string = 'May 9 2017 9:00AM'
date_datetime = datetime.strptime(date_string, '%b %d %Y %H:%M%p')
date_datetime.hour 


# In[19]:


import datetime

date_datetime += timedelta(hours=1)
a = datetime.datetime(date_datetime.year,date_datetime.month,date_datetime.day,date_datetime.hour,date_datetime.minute)
print(a)


# In[21]:


date_datetime.strftime( '%Y-%m-%d' )


# In[26]:


import datetime
from datetime import datetime, timedelta

a = []
startDate = '2017-01-01 00:00:00'
endDate = '2017-01-07 00:00:00'

startDate_datetime = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S')
endDate_datetime = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')

current_hour = startDate_datetime
while current_hour < endDate_datetime:
    a.append(current_hour.strftime('%Y-%m-%d %H:%M:%S'))
    current_hour += timedelta(hours=1)
    
print(a[-1])


# In[79]:


import datetime
from datetime import datetime, timedelta
import pandas as pd
import time

def make_unix_time(row):
    return time.mktime(row['datetime'].timetuple())

def convert_to_datetime(row):
    return datetime.strptime(row['date'], '%d.%m.%Y %H:%M')

data = pd.read_csv('https://raw.githubusercontent.com/dm-fedorov/pandas_basic/master/data/data.tsv', sep='\t')
data['datetime'] = data.apply(convert_to_datetime, axis=1)

data['unixtime'] = data.apply(make_unix_time, axis=1)

d1 = data.groupby('user_id')['unixtime'].apply(list)
min1 = []
max1 = []

for i in d1.index:
    min1.append(min(d1[i]))
    max1.append(max(d1[i]))
    
print('min = ',min1)
print('max = ',max1)


# In[81]:


a = []
leng = len(min1)
for i in range(leng):
    a.append(max1[i]-min1[i])

df = pd.DataFrame({'user_id': d1.index, 'diff': a})

df


# In[90]:


df.query('diff > 0', inplace = True)
life = df['diff'].values.mean()
print(life)


# In[93]:


print(round(life/(24*60*60),1))


# In[ ]:




