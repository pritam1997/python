"""Generate Complex number by user input"""
print(__doc__)
print("\n")
n = input("Enter 2 no. by comma seperated : ").split(",")
if len(n) > 2 or len(n) <2:
	print("Complex no. must be two no......!!!!!! ")
else:
	print(f"{n[0]}+{n[1]}j")