s=input("Enter String :")

def palind(s):
	d=""
	for x in range(1,len(s)+1):
		d+=s[-x]
	print(f"Original String : {s}")
	print(f"Reverse String : {d}")
	if s==d:
		print("String is palindrome")
	else:
		print("String is not palindrome")

palind(s)