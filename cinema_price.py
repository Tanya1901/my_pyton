Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def cin(x,y,z,d):
	if y=='завтра':
		if  d>=20:
			if x=='Паразиты':
				if int(z)==12:
					return 250*0.95*0.8*d
				elif int(z)==16:
					return 350*0.95*0.8*d
				elif int(z)==20:
					return 450*0.95*0.8*d
				else:
					print ('нет сеанса')
			elif x=='1917':
				if int(z)==10:
					return 250*0.95*0.8*d
				elif int(z)==13:
					return 350*0.95*0.8*d
				elif int(z)==16:
					return 350*0.95*0.8*d
				else:
					print ('нет сеанса')
			elif x=='Соник в кино':
				if int(z)==10:
					return 250*0.95*0.8*d
				elif int(z)==14:
					return 450*0.95*0.8*d
				elif int(z)==18:
					return 450*0.95*0.8*d
				else:
					print ('нет сеанса')
		else:
			if x=='Паразиты':
				if int(z)==12:
					return 250*0.95*d
				elif int(z)==16:
					return 350*0.95*d
				elif int(z)==20:
					return 450*0.95*d
				else:
					print ('нет сеанса')
			elif x=='1917':
				if int(z)==10:
					return 250*0.95*d
				elif int(z)==13:
					return 350*0.95*d
				elif int(z)==16:
					return 350*0.95*d
				else:
					print ('нет сеанса')
			elif x=='Соник в кино':
				if int(z)==10:
					return 250*0.95*d
				elif int(z)==14:
					return 450*0.95*d
				elif int(z)==18:
					return 450*0.95*d
				else:
					print ('нет сеанса')
	else:
		if  d>=20:
			if x=='Паразиты':
				if int(z)==12:
					return 250*0.8*d
				elif int(z)==16:
					return 350*0.8*d
				elif int(z)==20:
					return 450*0.8*d
				else:
					print ('нет сеанса')
			elif x=='1917':
				if int(z)==10:
					return 250*0.8*d
				elif int(z)==13:
					return 350*0.8*d
				elif int(z)==16:
					return 350*0.8*d
				else:
					print ('нет сеанса')
			elif x=='Соник в кино':
				if int(z)==10:
					return 250*0.8*d
				elif int(z)==14:
					return 450*0.8*d
				elif int(z)==18:
					return 450*0.8*d
				else:
					print ('нет сеанса')
		else:
			if x=='Паразиты':
				if int(z)==12:
					return 250*d
				elif int(z)==16:
					return 350*d
				elif int(z)==20:
					return 450*d
				else:
					print ('нет сеанса')
			elif x=='1917':
				if int(z)==10:
					return 250*d
				elif int(z)==13:
					return 350*d
				elif int(z)==16:
					return 350*d
				else:
					print ('нет сеанса')
			elif x=='Соник в кино':
				if int(z)==10:
					return 250*d
				elif int(z)==14:
					return 450*d
				elif int(z)==18:
					return 450*d
				else:
					print ('нет сеанса')

					
>>> x=input('Выберете фильм (Паразиты, 1917, Соник в кино):')
y=input('Сегодня или завтра:')
z=int(input('Выберете время:'))
d=int(input('Введите количество билетов:'))
SyntaxError: multiple statements found while compiling a single statement
>>> x=input('Выберете фильм (Паразиты, 1917, Соник в кино):')
Выберете фильм (Паразиты, 1917, Соник в кино):Паразиты
>>> y=input('Сегодня или завтра:')
Сегодня или завтра:завтра
>>> z=int(input('Выберете время:'))
Выберете время:12
>>> d=int(input('Введите количество билетов:'))
Введите количество билетов:21
>>> cin(x,y,z,d)
3990.0
>>> 