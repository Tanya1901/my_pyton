#!/usr/bin/env python
# coding: utf-8

# In[11]:


a = 0
A = 0
cif = 0
pr = 0
slov = 0
with open("Desktop/среднее.txt", encoding =  "utf-8") as file:
    rd = file.read()
    for zn in rd:
        if zn.isdigit():
            cif = cif + 1
        elif zn.islower() and zn != "n":
            a = a + 1
        elif zn.isupper():
            A = A + 1
        elif zn == " ":
            pr = pr + 1
with open("Desktop/среднее.txt", encoding =  "utf-8") as file:
    rd1 = file.readlines()
    rd2 = str(rd1).split()
    slov = len(rd2)
print("Среднее количество слов: ", slov/len(rd1))
print("Количество маленьких букв: ", a)
print("Количество больших букв: ", A)
print("Количество цифр: ", cif)
print("Количество пробелов: ", pr)
        


# In[ ]:





# In[ ]:





# In[ ]:




