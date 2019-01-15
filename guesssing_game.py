import random
print("guessing game between 1 to 10 number")
n = int(input("Enter no. :"))
r = random.randint(1,10)
if n == r: 
	print(f"Your no. {n} is matched")
elif n > 10:
	print("Your no. is greater than 10")
else:
	print("Fail!!!.. Try again..")
print(r)