import random
print("guessing game between 1 to 10 number")
n = int(input("Enter no. :"))
r = random.randint(1,10)
if n < 10:
	if n == r: 
		print(f"Your no. {n} is matched")
	elif n > r:
		print("Your no. is too large")
	else:
		print("your no. is too small")
else:
	print("Invalid input")
print(r)