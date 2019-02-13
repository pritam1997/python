l = []
n = int(input("How much no. you want to insert in List : "))

for x in range(1,n+1):
	i = int(input(f"No. {x} : "))
	l.append(i)

def odd(l):
	s=0
	for x in l:
		if x%2!=0:
			s=s+x
	print(s)

odd(l)
