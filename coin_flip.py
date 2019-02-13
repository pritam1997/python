import random

ai=random.randint(1,2)
s = input(" Choose Head or Tail :")

if ai==1:
	ai="head"	
else:
	ai="tail"
if s.lower()=="head" or s.lower()=="tail":
	print(f"Coin flipped : {ai}")
	if ai==s:
		print("You win")
	else:
		print("You lose")
else:
	print("Please enter as per mention above.")