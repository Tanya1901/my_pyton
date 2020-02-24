Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(x):
	if -2.4<=float(x)<=5.7:
		return pow(float(x),2)
	else:
		return 4

	
>>> f(3.5)
12.25
>>> f(5)
25.0
>>> f(7)
4
>>> 