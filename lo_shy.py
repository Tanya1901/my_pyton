#!/usr/bin/env python
# coding: utf-8

# In[11]:


from random import randint
b=[[randint(1,9) for _ in range(3)] for x in range(3)]
b


# In[30]:


for i in range(3):
    for j in range(3):
        sum1=sum2=sum3=sum0=0
        sum1=sum1+int(b[0][j])
        sum2=sum2+int(b[1][j])
        sum3=sum3+int(b[2][j])
        sum0=sum0+int(b[i][j])
if (sum1==15) and (sum2==15) and (sum3==15) and (sum0==45):
    print('Магический квадрат Ло Шу')
else:
    print('Не Магический квадрат Ло Шу')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




