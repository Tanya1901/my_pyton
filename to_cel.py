#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
def click():
    converter.set (round(5/9*(float(entry.get())-32),3))
window = Tk()
frame = Frame(window)
frame.pack()
converter = IntVar()
entry = Entry(frame)
entry.pack()
label = Label(frame, textvariable=converter)
label.pack()
button = Button(frame, text='Перевести в градусы Цельсия', command=click)
button.pack()
button1 = Button(frame,text="Выход",command=exit)
button1.pack()

window.mainloop()


# In[ ]:





# In[ ]:




