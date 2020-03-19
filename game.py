#!/usr/bin/env python
# coding: utf-8

# In[60]:


class Person:
    def __init__(self,name='Персонаж',x=0,y=0):
        self.name = name
        self.__x = x
        self.__y = y
        print((x,y))
        
    def run(self, delta_x=2, delta_y=0):
        print('Побежали!')
        self.__x = self.__x + delta_x
        self.__y = self.__y + delta_y
        print((self.__x,self.__y))
        
    def shoot(self, delta_x=0, delta_y=0):
        print('Прицелься!')
        self.__x = self.__x * delta_x
        self.__y = self.__y + delta_y
        print((self.__x,self.__y))
        
    def pick(self, delta_x=3, delta_y=1):
        print('Поднимай!')
        self.__x = self.__x + 0
        self.__y = self.__y - 1
        print((self.__x,self.__y))
        self.__x = self.__x + delta_x
        self.__y = self.__y + delta_y
        print((self.__x,self.__y))

class Flying(Person):
    def __init__(self,name='Летающий персонаж',x=1,y=1):
        Person.__init__(self,x=x,y=y,name=name)
        self.__x = x
        self.__y = y
        print('Я умею летать!')
    def fly(self,x=1,y=1,delta_x=2,delta_y=1):
        print('Полетели!')
        self.__x = self.__x + delta_x
        self.__y = self.__y + delta_y
        print((self.__x,self.__y))
        self.__x = self.__x + 0
        self.__y = self.__y - 1
        print((self.__x,self.__y))
            


# In[ ]:





# In[61]:


person = Person('Иван',1,1)
person.run()



fl = Flying('Игорь')
fl.fly()


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




