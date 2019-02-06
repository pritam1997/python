stud0 = {"id":"01",
		"name":{
			"firstname":"Connor",
			"middlename":"Haytham",
			"lastname":"Kenway"},
		"location":{
			"line_1":"644-Block",
			"line_2":"Boston",
			"line_3":"USA"}}
# stud1 = {"id":"01",
# 		"name":{
# 			"firstname":"Connor",
# 			"middlename":"Haytham",
# 			"lastname":"Kenway"},
# 		"location":{
# 			"line_1":"644-Block",
# 			"line_2":"Boston",
# 			"line_3":"USA"}}
# stud2 = {"id":"01",
# 		"name":{
# 			"firstname":"Connor",
# 			"middlename":"Haytham",
# 			"lastname":"Kenway"},
# 		"location":{
# 			"line_1":"644-Block",
# 			"line_2":"Boston",
# 			"line_3":"USA"}}
# stud3 = {"id":"01",
# 		"name":{
# 			"firstname":"Connor",
# 			"middlename":"Haytham",
# 			"lastname":"Kenway"},
# 		"location":{
# 			"line_1":"644-Block",
# 			"line_2":"Boston",
# 			"line_3":"USA"}}
l=[]
stud0={"asd":"sdsd","asdsad":{"werwer":"trtr"}}
for k in stud0.items():
	l.append(k)

# print(l)
for i in l[:]:
	l[i]=list(i)
print(l)