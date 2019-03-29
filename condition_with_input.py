"""If you enter digit or character one it display as it is and more than one 
it will display concatenate."""

# print(__doc__)
n = input("Enter byte with comma(,) seperated : \n").split(',')

if len(n) ==1:
	print(n[0])
elif len(n) >1:
	s=str()
	for i in range(len(n)):
		s=s+n[i]
	if s.isdigit():
		c = input("Choose concatenate for [1] or sum for [2] : ")
		if c == '1':
			print(s)
		elif c=='2':
			sum=0
			for i in range(len(n)):
				sum=sum+int(n[i])
			print(sum)
	elif s.isalpha() or s.isalnum():
		print(s)

