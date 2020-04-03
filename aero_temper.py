#!/usr/bin/env python
# coding: utf-8

# In[9]:



import matplotlib.pyplot as plt
a=[]
t=[]
s=0
with open('Desktop/temper.txt') as file:
    lines = file.readlines()
    for line in lines:
        if lines.count(line) == 1:
            line = line.replace('\n','')
            line = line.replace(',','.')
            line = line.replace('+','')
            a.append(float(line))
        else:
            line = line.replace('\n','')
            line = line.replace(',','.')
            line = line.replace('+','')
        t.append(float(line))
        s += float(line)
    print("Максимальное значение: ", max(t))
    print("Минимальное значение: ", min(t))
    print("Среднее значение: ", s/len(t))
    print("Количество уникальных значений: ", len(a))
    fig = plt.figure()
    plt.bar(range(len(t)),t)
    plt.grid(True)
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[27]:


a=[1,2,3,2]
a.count(2)


# In[27]:


a=[1,2,3,2]
a.count(2)


# In[ ]:





# In[1]:


list(set([1,2,3,2,3]))


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




