#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


a = []
while True:
    read = input()
    if read.isdigit():
        a.append(int(read))
        print(a)
    elif read == '+':
        a.append(int(a.pop()) + int(a.pop()))
        print(a)
    elif read == '-':
        a.append(int(-a.pop()) + int(a.pop()))
        print(a)
    elif read == '*':
        a.append(int(a.pop()) * int(a.pop()))
        print(a)
    elif read == '/':
        b = int(a.pop())
        c = int(a.pop())
        a.append(c/b)
        print(a)
        
    
    


# In[ ]:





# In[ ]:





# In[ ]:




