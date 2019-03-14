n=int(input("ENter no. : "))
i=2
l=[0,1]
while i<=n:
	a=l[i-1]+l[i-2]
	l.append(a)
	i+=1
for i in l:
	print(i)