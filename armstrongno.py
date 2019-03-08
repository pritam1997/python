n=int(input("Enter number to check armstrong number : "))
s=str(n)
s1=0

for i in s:
	n=int(i)
	n=n*n*n
	s1+=n
	print(s1)

if str(s1)==s:
	print(f"{s} is an armstrong number")
else:
	print(f"{s} is not armstrong number")