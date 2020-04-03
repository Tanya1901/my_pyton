#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    o = input("Введите операцию: ")
    if o in ('+','-','*','/'):
        if o == '+':
            print (x+y)
        elif o == '-':
            print (x-y)
        elif o == '*':
            print (x*y)
        else:
            print (x/y)
    else:
        print ("Введена неверная операция!")
except ZeroDivisionError:
    print("Ошибка деления на ноль!!!")
except ValueError:
    print("Ошибка преобразования типа!!!")
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


cal

