import random

def even(a):
	if a%2==0:
		print(a)

for x in range(1,101):
	a=random.randint(1,100)	
	even(a)


