l = []

print("TO END YOUR INPUT WRITE \"[ END or end]\"\n")
x=0

while x>=0:
	a=str(input("Enter value : "))

	if a=="":
		print("********\\        Please enter any value       \\*********")
	else:
		l.append(a)

	if a=="END" or a=="end":
		break

	x+=1

l.pop()
print(l)
