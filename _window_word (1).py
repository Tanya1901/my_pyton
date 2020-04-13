#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
import random
 
d = {'cat':'кот' , 'dog':'собака', 'elephant':'слон', 'car':'машина', 'three':'дерево', 'house':'дом'}
r = random.choice(list(d.keys()))

window = Tk()
window.geometry('200x190')  
 
def click():
    answer = d.get(r)
    if entry.get() == answer:
        result = 'Верно!'
        label_result.config(text=result)
    else:
        result = 'Не верно!'
        label_result.config(text=result)

frame_name = Frame(window)
frame_name.pack()
frame_question = Frame(window)
frame_question.pack()
frame_eng = Frame(window)
frame_eng.pack()
frame_butn = Frame(window)
frame_butn.pack()
frame_result = Frame(window)
frame_result.pack()
 
label_question = Label(frame_question, text=r)
label_question.pack()
label_name = Label(frame_name, text='Укажите перевод слова:')
label_name.pack()
entry = Entry(frame_eng)
entry.pack()
label_result = Label(frame_result)
label_result.pack()
 
button = Button(frame_butn, text='Проверка', command=click)
button.pack()
button1 = Button(frame_eng, text="Выход",command=exit)
button1.pack()


window.mainloop()


# In[ ]:





# In[ ]:




