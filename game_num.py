#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
a=random.choice(range(10))
while True:
    c=1;
    n=input('Введите число или выход: ')
    if n=='Выход' or c==4 :
        print('Выход из программы! До встречи!')
        break
    elif int(n)<a:
        print('больше')
        c+=1
    elif int(n)>a:
        print('меньше')
        c+=1
    else:
        print('Молодец!')
        break


# In[ ]:




