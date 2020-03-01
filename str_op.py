Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "У лукоморья 123 дуб зеленый 456"
>>> 
>>> s.rindex('я',1,len(s))

10
>>> s.count('у',1,len(s))

2
>>> if s.isalpha():
    s
else:
    s.upper()

    
'У ЛУКОМОРЬЯ 123 ДУБ ЗЕЛЕНЫЙ 456'
>>> if len(s)>4:
    s.lower()
else:
    s

    
'у лукоморья 123 дуб зеленый 456'
>>> s.replace(s[0],'О')
'О лукоморья 123 дуб зеленый 456'
>>> 