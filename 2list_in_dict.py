mylist1=["saurabh","ankit","sumit","mohammad"]
mylist2=["chauhan","trivedi","chandak","rafiq"]
lis2=[[],[],[],[]]

for x in range(0,len(mylist1)):
	lis2[x].append(mylist1[x])
	lis2[x].append(mylist2[x])

d=dict(lis2)
print(f"\n******* Dictionaries :\n {d}")