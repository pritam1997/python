p1=input("player 1:")
p2=input("player 2:")


if p1==rock and p2==scissor:
print("player 1 wins ")

elif p1==scissor and p2==rock:
print("player 2 wins")

elif p1==paper and p2==rock:
print("player 1 wins")

elif p1==rock and p2==paper:
	print("player 2 wins")

elif p1==paper and p2==scissor:
	print("player 2 wins")

elif p1==scissor and p1==paper:
print("player 1 wins")



