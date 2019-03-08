s=int(input("Enter no. to print triangle : "))
n=1
for i in range(s-1,-1,-1):
	print(" "*i,"*"*n)
	n+=2
