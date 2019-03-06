class student:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	
	
	def student_details(self):
		return f"{self.name.capitalize()},{self.rollno}"

	def standard(self,std):
		if std<1 or std>10:
			print("Standard upto 1 to 10")
		else:
			c=str(std)
			if c[-1]=='1':
				e='st'
			elif c[-1]=='2':
				e='nd'
			elif c[-1]=='3':
				e='rd'
			else:
				e='th'
			return f"{self.name.capitalize()} studying in {std}{e} Standard"
	
	def percentage(self,percent):
		if percent<35:
			print("Failed student")
		elif percent>35 and percent<49:
			print("Poor student")
		elif percent<50 and percent<59:
			print("Satisfactory student")
		elif percent>60 and percent<69:
			print("Good student")
		elif percent>70 and percent<84:
			print("Very Good student")
		elif percent>85:
			print("Excellent")
		return f"{percent}%"

	def age(self,ag):
		return f"{self.name.capitalize()} is {ag} year old"

	def dob(self,date,mon,yr):
		if yr <1998 or yr >2018:
			print("Only 1998 to 2014 years students are allow")
		else:
			n=2019-yr
			print(self.age(n))	
		return f"{self.name.capitalize()} birthday on {date}-{mon}-{yr}"

	def sports(self,sp):
		return f"{self.name.capitalize()} is interested in {sp}"

s=student("sujit",12)
a=s.standard(9)
print(a)
a=s.percentage(75)
print(a)
a=s.dob(10,12,1999)
print(a)
a=s.sports("football")
print(a)

print("\n")

s1=student("rohit",34)
a=s1.standard(3)
print(a)
a=s1.percentage(80)
print(a)
a=s1.dob(1,2,2015)
print(a)
a=s1.sports("chess")
print(a)
