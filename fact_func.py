n=int(input("Enter no. : "))

def fact(n):
	f=1
	while n>0:
		f=f*n
		n-=1
	print(f)

fact(n)