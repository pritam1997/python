from random import random

print("\n")
print("---------Lets guess your luck with your name------------")
print("\n")

s=str(input("Enter your name : "))

if len(s)==0:
	exit(0)

r=random()

if r<0.5:
	print("!!!!!!!!Unlucky.......")
else:
	print("@@@@@@You are lucky....")