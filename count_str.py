# s=input("Enter string : ")
s="asdasdq"
def fun(s):
	l=len(s)
	c=1
	
	for x in range(l):
		if x==0:
			a=1
		elif x==1:
			a=2
		elif x==2:
			a=3
		elif x==3:
			a=4
		elif x==4:
			a=5
		for i in range(a,l):
			if x==i:
				break		
			if s[x]==s[i]:
				c+=1
				t=c

	print(t)
	# a=input("which letter you want to count : ")
	# c=s.count(a)
	# return c
fun(s)