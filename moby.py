#!/usr/bin/env python
# coding: utf-8

# In[13]:


with open('Desktop/moby.txt') as file:
    for line in file:
        line = line.lower()
        for sim in line:
            if sim in ['\n','.',',','-',':',';','?','!','...','(',')','"']:
                line = line.replace(sim,'')
        line = line.split(' ')
        for word in line:
            with open("moby_clean.txt", 'a') as output_file:
                output_file.write(word + '\n')


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





# In[1]:


with open('Desktop/moby.txt') as file:
    lines = list(file.readlines())
    for line in lines:
        for word in line:
            a=[]
            while word != ' ':
                a.append(word)
            print(a)


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




