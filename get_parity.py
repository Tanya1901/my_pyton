Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def even(x):
	if int(x)==x:
		if x%2==0:
			print ('четное число')
		else:
			print ('нечетное число')
	else:
		print('введите целое число')

		
>>> even(5.4)
введите целое число
>>> even(7)
нечетное число
>>> 