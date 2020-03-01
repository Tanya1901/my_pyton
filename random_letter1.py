Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> 
def f(s):
    a = str(random.choice(s))
    print('Выбираем случайное слово: ', a)
    b = str(random.choice(a))
    print('Выбираем случайную букву: ', b)
    print(a[0 : a.index(b, 0, len(a))],'?', a[a.index(b, 0, len(a)) + 1 : len(a) + 1])
    d = input(str('Вставьте букву: '))
    if d == b:
        print('Верно')
        print('Слово: ', a)
    else:
        print('попробуй еще раз')
        print('Слово: ', a)

        
>>> 
>>> s = ['самовар', 'весна', 'лето']
>>> f(s)
Выбираем случайное слово:  самовар
Выбираем случайную букву:  м
са ? овар
Вставьте букву: м
Верно
Слово:  самовар
>>> 