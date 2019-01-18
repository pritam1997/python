import random
print("Rock Paper Scissor Game :\n")
ai = random.randint(1,3)

if ai == 1:
	p1 = "rock"
elif ai == 2:
	p1 = "paper"
else:
	p1 ="scissor"

# print(f"Player 1, choice of computer is : {p1}")
p2 = str(input("Player 2 Enter your choice :")).lower()

if p1 == p2:
	print("Tie")
elif p1 == "rock":
	if p2 == "scissor":
		print("Player 1 win")
	elif p2 == "paper":
		print("Player 2 win")

elif p1 == "paper":
	if p2 == "scissor":
		print("Player 2 win")
	elif p2 == "rock":
		print("Player 1 win")

elif p1 == "scissor":
	if p2 == "rock":
		print("Player 2 win")
	elif p2 == "paper":
		print("Player 1 win")
else:
	print("something went wrong ")