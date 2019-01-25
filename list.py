fruits = [ "apple","mango","banana","strawbery","Grapes"]

for x in fruits:
	print(x.upper())

x = fruits.append(12)
print("Append value : ",fruits)

x = fruits.pop()
print("\nPoped value", fruits)

x = fruits.sort()
print("\nSorted value : ",fruits)

x = fruits.extend((12,23))
print("\nExtended value : ",fruits)

x = fruits.insert(2,"Flowers")
print("\nInserted value : ",fruits)

x = fruits.remove("Flowers")
print("\nRemoved value : ", fruits)

x = fruits.index("banana")
print("\nIndex value : ", fruits)

x = fruits.count("apple")
print("\nCount value : ", fruits)

x = fruits.clear()
print("\nValue is being cleared : ", fruits)

