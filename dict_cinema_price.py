#!/usr/bin/env python
# coding: utf-8

# In[3]:


films = {"Паразиты": {'time': {12: 250, 14: 350, 16: 450}}, "1917": {'time': {10: 250, 13: 350, 16: 350}}, "Соник в кино": {'time': {10: 350, 14: 450, 18: 450}}}
x = input('Выберете фильм (Паразиты, 1917, Соник в кино):')
y = input('Сегодня или завтра:')
z = int(input('Выберете время:'))
d = int(input('Введите количество билетов:'))
price = films[x]['time'][z]
if y == 'завтра':
    if int(d) >= 20:
        price = 0.75 * price
    else:
        price = 0.95 * price
else:
    if int(d) >= 20:
        price = 0.8 * price

print(price * d)
        
    


# In[ ]:




