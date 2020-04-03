#!/usr/bin/env python
# coding: utf-8

# In[11]:


import random

a = str(input("Введите свой общий вопрос или break: "))

if a != "break":
    with open("Desktop/шар.txt") as file:
        rd = file.readlines()
        rd_r = random.choice(rd)
        print(rd_r.strip())
        a = str(input("Введите свой общий вопрос или break: "))
else:
    print("Спасибо за вопрос(ы)!")
        


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





# In[10]:


import random
with open("Desktop/шар.txt") as file:
        reader = file.readlines()
        print(random.choice(reader))


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




