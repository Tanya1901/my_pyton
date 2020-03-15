#!/usr/bin/env python
# coding: utf-8

# In[4]:


for j in range(20): 
    a[j]=int(input())
max1=a[0]+a[1]+a[2]+a[3]+a[4]
s=max1
mi=4
for i in range(1,16):
    s = a[i] + a[i+1] + a[i+2] + a[i+3] + a[i+4]
    if s > max1:
        mi = i
        max1 = s
print('Максимальная сумма: ', max1, 'Элементы: ',a[mi],' ',a[mi+1],' ',a[mi+2],' ',a[mi+3],' ',a[mi+4])


# ## 

# In[6]:


a = []
for j in range(20):
    a.append(int(input()))
max1=int(a[0])+int(a[1])+int(a[2])+int(a[3])+int(a[4])
s=max1
mi=4
for i in range(1,16):
    s = int(a[i])+int(a[i+1])+int(a[i+2])+int(a[i+3])+int(a[i+4])
    if s > max1:
        mi = i
        max1 = s
print('Максимальная сумма: ', max1, 'Элементы: ',a[mi],' ',a[mi+1],' ',a[mi+2],' ',a[mi+3],' ',a[mi+4])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




