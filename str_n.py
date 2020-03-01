Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def f(s,n):
	if len(s)>n:
		return s.upper()
	else:
		return s

	
>>> s='jwhvx,ercfr'

>>> f(s,3)
'JWHVX,ERCFR'
>>> 