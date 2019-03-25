""" ---------------- Copy no. file content into one file -------------------- """
print(__doc__)
n =int(input ("How many no. of file you have : "))

#	To erase content of target file
file = open("alltext.txt","w+")
print(file.tell())
file.truncate()
file.read()
file.close()


for i in range(1,n+1):

	# Note : you must have filename from which content will copy

	for line in open(f"test{i}.txt",'r'):
		file = open(f"alltext.txt","a")
		file.write(line)
	file.write(f"\n ------------------file{i}------------------------\n")
	file.close()
	print(f"Content of File{i} is pasted in alltext.txt")

