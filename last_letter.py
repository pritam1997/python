s = input("Enter any word : ")
c=len(s)

def word(s,c):
	print(f"Last letter of word is : {s[-1]}")

def sent(s,c):
	n=0
	for x in range(-1,-c,-1):
		n+=1
		if s[x] == " ":
			break
	print(f"\n-------Last word of sentence is : ---------")
	for a in range(-n+1,0):
		print(f"------{s[a]}------")
word(s,c)
sent(s,c)