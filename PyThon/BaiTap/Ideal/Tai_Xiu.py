import random
a=random.randrange(1,7)
b= random.randrange(1,7)
c= random.randrange(1,7)

def taixiu(a,b,c):
	d= a+b+c
	if d > 10:
		print('tai',d)
	else:print('xiu',d)

taixiu(a,b,c)

