name=str(input("Enter name : "))

ch=str(input("$$$$$$$$$$$ Do you want to call (y / n): "))
def first(name):
	print(f"\n{name} is a person called a function")
	return 0
if ch.lower()=="y":
	first(name)
elif ch.lower()=="n":
	print("Thank you come back again!!")
else:
	print("!!!Please enter as mentioned above ...")