print("Rock Scissor Paper Game :\n")
p1 = str(input("Enter Player 1 choice : ")).lower()

print("**** NO CHEATING \n\n"*30)

p2 = str(input("Enter Player 2 choice : ")).lower()

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

# if p1 == "rock" and p2 == "scissor":
# 	print("Player1 win")
# elif p1 == "rock" and p2 == "paper":
# 	print("Player2 win")
# elif p1 == "rock" and p2 == "rock":
# 	print("Tie")

# elif p1 == "paper" and p2 == "rock":
# 	print("Player 1 win")
# elif p1 == "paper" and p2 == "scissor":
# 	print("Player2 win")
# elif p1 == "paper" and p2 == "paper":
# 	print("Tie")

# elif p1 == "scissor" and p2 == "scissor":
# 	print("Tie")
# elif p1 == "scissor" and p2 == "paper":
# 	print("Player1 win")
# elif p1 == "scissor" and p2 == "rock":
# 	print("Player 2 win")