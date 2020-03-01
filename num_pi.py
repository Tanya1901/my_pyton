Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fixed(numObj, digits=0):
	return f"{numObj:.{digits}f}"

>>> import math
>>> fixed(math.pi,3)
'3.142'
>>> 