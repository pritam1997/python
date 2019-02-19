s=input("Enter string : ")
def fun(s):
	l=list(s)
	for i in s:
		print(f"{i} = {l.count(i)}")
fun(s)