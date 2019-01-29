d={"id":"01","firstname":"Haytham","lastname":"Kenway","location":"Boston"}
d2 ={"id":"02", "firstname":"Connor", "lastname":"Kenway", "location":"Rome"}
ids={}
firstname={}
lastname={}
location={}

for k,v in d.items():
	if k=="id":
		ids={k:v}
	if k=="firstname":
		firstname={k:v}
	if k=="lastname":
		lastname={k:v}
	if k=="location":
		location={k:v}
	
print(ids)
print(firstname)
print(lastname)
print(location)
print(d)

d["firstname"]="Pritam"
d["lastname"]="Vishwakarma"

for k,v in d.items():
	if k=="id":
		ids={k:v}
	if k=="firstname":
		firstname={k:v}
	if k=="lastname":
		lastname={k:v}
	if k=="location":
		location={k:v}
print("\n")
print(ids)
print(firstname)
print(lastname)
print(location)
print(d)
