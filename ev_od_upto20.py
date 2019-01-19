# n = 0
# while n < 21:
# 	if n % 2 == 0:
# 		if n == 4 or n == 13:
# 			print(f"{n} is unlucky no.")
# 		print(f"{n} is even no.")
# 	else:
# 		print(f"{n} is odd no.")
# 	n += 1


for n in range(0,21):
	if n == 4 or n == 13:
		print(f"{n} is unlucky no.")
	elif n%2 == 0:
		print(f"{n} is even..!!")
	else:
		print(f"{n} is odd...!!")