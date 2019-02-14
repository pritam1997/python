t=int(input("Which no. table do you want : "))
def table(t):
	for x in range(1,11):
		print(f"{t} x {x} = {x*t}")

table(t)