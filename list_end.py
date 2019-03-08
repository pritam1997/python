def start_ends_list(n):
	l=[n*i for i in range(1,11)]
	l1=[]
	l1.append(l[0])
	l1.append(l.pop())
	print(l1)

start_ends_list(5)