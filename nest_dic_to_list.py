stud1 = {"id":"01",			#0
		"name":{			#1	
			"firstname":"Connor",	
			"middlename":"Haytham",
			"lastname":"Kenway"},
		"location":{		#2
			"line_1":"644-Block",
			"line_2":"Boston",
			"line_3":"USA"}}

l=[]
for k,v in stud1.items():
	if k=="id":
		l.append([k,v])
	if k=="name":
		l.append([k])
		for x in stud1["name"].items():
			m=list(x)
			l[1].append(m)
	if k=="location":
		l.append([k])
		for x in stud1["location"].items():
			m=list(x)
			l[2].append(m)
	
print(l)