s = input("Enter string : ")
def fun(s):
	n=len(s)
	c=0
	l=[]
	for i in range(-1,-n,-1):
		if s[i]== " ":
			break
		c+=1

	for x in range(-c,0):
		s.append(s[x])
	f=str(l)
	print(f)
fun(s)