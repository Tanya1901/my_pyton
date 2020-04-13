#!/usr/bin/env python
# coding: utf-8

# In[46]:


from tkinter import *
from tkinter import scrolledtext  

import json
with open("to__do.json","w") as f:
    listt=[]
    def clear():
            task.delete(0,END)
            cat.delete(0,END)
            time.delete(0,END)
    def send():
        a=json.dump({"задача":task.get(),"категория":cat.get(),"время":time.get()},f)
        listt.append({"задача":task.get(),"категория":cat.get(),"время":time.get()})
        clear()
    def tasks():
        txt.delete(1.0, END)
        for elements in listt:
            for element in elements:
                txt.insert(INSERT,element)
                txt.insert(INSERT,":")
                txt.insert(INSERT,elements[element])
                txt.insert(INSERT, " ")
            txt.insert(INSERT, "\n")
            
    def quit():
        print("Выход из программы")
    
    window=Tk()
    window["bg"]="pink"
    window.title("Менеджер задач")
    task_list=Label(window,bg="pink")
    task_label=Label(window,text="Задача:",bg="pink")
    cat_label=Label(window,text="Категория:",bg="pink")
    time_label=Label(window,text="Время:",bg="pink")
    task_label.grid(row=0,column=0)
    cat_label.grid(row=1,column=0)
    time_label.grid(row=2,column=0)
    task=Entry(window)
    cat=Entry(window)
    time=Entry(window)
    task.grid(row=0,column=1,columnspan=2)
    cat.grid(row=1,column=1,columnspan=2)
    time.grid(row=2,column=1,columnspan=2)
    window.geometry('550x180')  
    txt = scrolledtext.ScrolledText(window,width=40, height=10)  
    txt.grid(column=3, row=0,rowspan=6,columnspan=4)  
    button1=Button(window,text="Заказать",command=send,bg="lightpink")
    button2=Button(window,text="Список задач",command=tasks,bg="lightpink")
    button3=Button(window,text="Выход",command=quit,bg="lightpink")
    button1.grid(row=3,column=1)
    button2.grid(row=4,column=1)
    button3.grid(row=5,column=1)
    
    window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




