from random import random

print("\n")
print("---------Lets guess your luck------------")
print("\n")

s=str(input("Enter your name : "))

if len(s)==0:
	exit(0)

r=random()

if r>=0.5:
	print("@@@@@@You are lucky....")
else:
	print("!!!!!!!!Unlucky.......")
