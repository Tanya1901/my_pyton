#!/usr/bin/env python
# coding: utf-8

# In[1]:


a='Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог'


# In[2]:



print(' '.join(x for x in a.split(' ') if not x.startswith('м')))


# In[ ]:




