age = int(input("Enter your age to valid for entry :"))
if age >= 18 and age <= 21:
	print("Take Wrist Band you are able to enter in party.\nBut not permission to drink alcohol.")
elif age > 21:
	print("You can visit to the party.")
else:
	print("You are too young.\nThank you for coming.")
