#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = set()
a1 = set()
a2 = set()
with open("Desktop/среднее.txt", encoding =  "utf-8") as file:
    rd_sr = file.readlines()
    rd_sr2 = str(rd_sr).split()
    for w1 in rd_sr2:
        w1.replace("\n","")
        a1.add(w1)
        
with open("Desktop/шар.txt", encoding =  "utf-8") as file:
    rd_sh = file.readlines()
    rd_sh2 = set(str(rd_sh).split())
    for w2 in rd_sh2:
        w2.replace("\n","")
        a2.add(w2)

    for w in a1 & a2:
        if str(a1 & a2).count(w) == 1:
            a.add(w1)
print("Уникальные в обоих файлах: ", a)
print("В обоих файлах: ", a1 & a2)
print("Только в 1: ", a1.difference(a2))
print("Только во 2: ", a2.difference(a1))
print("Не в обоих: ", a1.symmetric_difference(a2))
        


# In[ ]:





# In[ ]:




