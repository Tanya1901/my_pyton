#!/usr/bin/env python
# coding: utf-8

# In[10]:


a = []
max = []
min = []
with open('moby_clean.txt') as file:
    lines = file.readlines()
    for line in lines:
        a.append(lines.count(line))
    for line in lines:
        if line != '\n':
            if len(list(set(max))) < 5:
                if lines.count(line) == list(set(a))[-1]:
                    line = line.replace('\n','')
                    max.append(line)
    if len(list(set(max))) < 5:
        for line in lines:
            if line != '\n':
                if len(list(set(max))) < 5:
                    if lines.count(line) == list(set(a))[-2]:
                        line = line.replace('\n','')
                        max.append(line)
    if len(list(set(max))) < 5:
        for line in lines:
            if line != '\n':
                if len(list(set(max))) < 5:
                    if lines.count(line) == list(set(a))[-3]:
                        line = line.replace('\n','')
                        max.append(line)
    if len(list(set(max))) < 5:
        for line in lines:
            if line != '\n':
                if len(list(set(max))) < 5:
                    if lines.count(line) == list(set(a))[-4]:
                        line = line.replace('\n','')
                        max.append(line)
    if len(list(set(max))) < 5:
        for line in lines:
            if line != '\n':
                if len(list(set(max))) < 5:
                    if lines.count(line) == list(set(a))[-5]:
                        line = line.replace('\n','')
                        max.append(line)   
                    
                    
    for line in lines:
        if line != '\n':
            if len(list(set(min))) < 5:
                if lines.count(line) == list(set(a))[0]:
                    line = line.replace('\n','')
                    min.append(line)
    if len(list(set(min))) < 5:
        for line in lines:
            if line != '\n':
                if len(list(set(min))) < 5:
                    if lines.count(line) == list(set(a))[1]:
                        line = line.replace('\n','')
                        min.append(line)
    if len(list(set(min))) < 5:
        for line in lines:
            if line != '\n':
                if len(list(set(min))) < 5:
                    if lines.count(line) == list(set(a))[2]:
                        line = line.replace('\n','')
                        min.append(line)
    if len(list(set(min))) < 5:
        for line in lines:
            if line != '\n':
                if len(list(set(min))) < 5:
                    if lines.count(line) == list(set(a))[3]:
                        line = line.replace('\n','')
                        min.append(line)
    if len(list(set(min))) < 5:
        for line in lines:
            if line != '\n':
                if len(list(set(min))) < 5:
                    if lines.count(line) == list(set(a))[4]:
                        line = line.replace('\n','')
                        min.append(line)
                    
                    
    print('Самые частые: ', list(set(max)))
    print('Самые редкие: ', list(set(min)))


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




