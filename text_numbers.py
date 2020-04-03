#!/usr/bin/env python
# coding: utf-8

# In[20]:


def num(name,update_name):
    s=0
    try:
        with open(name + '.txt') as file:
            lines = file.readlines()
            for line in lines:
                s+=1
                with open(update_name + ".txt", 'a') as output_file:
                    output_file.write(str(s) + ' ' + line + '\n')
    except:
        print('Файл не найден')


# In[21]:


num('example_text.txt','up_text')


# In[ ]:




