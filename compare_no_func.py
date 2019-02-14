n1 = int (input ("Enter 1st no. : "))
n2 = int (input ("Enter 2nd no. : "))

def comp(n1,n2):
	if n1 > n2 :
		print(f"{n1} is greater ")
	elif n1 == n2:
		print(f"Both are equal ")
	else:
		print(f"{n2} is smaller ")
comp(n1,n2)
