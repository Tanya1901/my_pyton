#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Human:
    def __init__(self,new_name= 'без имени'):
        self._name=new_name
        print(f'Родился человек с именем {self._name}')
        self.__age=1

    def eating(self):
        print(f'{self._name} ест')    

    def sleeping(self):
        print(f'{self._name} спит')

    def working(self):
        if 18<=self.__age<65:
            print(f'{self._name} работает')
        elif self.__age>=65:
            print(f'{self._name} на пенсии')
            
    def relaxing(self):
        print(f'{self._name} отдыхает')

    def growing(self):
        print(f'{self._name} отмечает день рождения')
        self.__age+=1


# In[2]:


class Life:
    def life(self, human, years=70):
        while years:            
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            years -= 1
        
petr = Human('Петр')
life_petr = Life()
life_petr.life(petr)


# In[ ]:




