Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li=3
>>> mn=25
\
>>> hg=80
>>> cl=17
>>> def chem(x):
	if x==li:
		print ('Это Li')
	elif x==mn:
		print ('Это Mn')
	elif x==hg:
		print ('Это Hg')
	elif x==cl:
		print ('Это Cl')
	else:
		print ('не знаю такой элемент')

		
>>> chem(35)
не знаю такой элемент
>>> chem(80)
Это Hg
>>> 