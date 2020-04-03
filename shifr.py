#!/usr/bin/env python
# coding: utf-8

# In[7]:


intab = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
outtab = "БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАбвгдеёжзийклмнопрстуфхцчшщъыьэюяа"
codes = str.maketrans(intab,outtab)
with open("Desktop/шар.txt", "r", encoding =  "utf-8") as file1, open("шар_1.txt", "w", encoding =  "utf-8") as file2:
    rd1 = file1.readlines()
    file2.writelines(str(rd1).translate(codes))
               


# In[9]:


intab = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
outtab = "БВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАбвгдеёжзийклмнопрстуфхцчшщъыьэюяа"
codes = str.maketrans(outtab, intab)
with open("шар_1.txt", "r", encoding =  "utf-8") as file:
    rd1 = file.read()
    print(str(rd1).translate(codes))
               


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




