class student:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	
	
	def student_details(self):
		return f"{self.name.capitalize()},{self.rollno}"

	def standard_marks(self,std,marks):
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
			return f"{self.name.capitalize()} got {marks}% in {std}{e} Standard"

	def age(self,ag):
		return f"{self.name.capitalize()} is {ag} year old"

	def dob(self,date,mon,yr):
		if yr <1998 or yr >2014:
			print("Only 1998 to 2014 birth student are allow")
		else:
			n=2019-yr
			print(self.age(n))	
		return f"{self.name.capitalize()} birthday on {date}-{mon}-{yr}"

	def sports(self,sp):
		return f"{self.name.capitalize()} is interested in {sp}"

s=student("sujit",12)
a=s.standard_marks(9,80)
print(a)
a=s.dob(10,12,1999)
print(a)
a=s.sports("football")

s1=student("rohit",34)
a=s1.standard_marks(3,90)
print(a)
a=s1.dob(1,2,2015)
print(a)
a=s1.sports("chess")

