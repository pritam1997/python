class stud:
	def __init__(s,firstname,lastname,rollno):
		s.firstname=firstname
		s.lastname=lastname
		s.rollno=rollno

	def student_details(s):
		return f"{s.firstname} {s.lastname}\t{s.rollno}"

	def stud_age(age):
		if age<5 or age>16:
			print("You are not eligible")
		elif age>16:
			print("Are you has backlog")

		

	def stud_dob(dob):

	def sports(s):
		return f"{s.sport}"

	def exam(s):
		return f"{s.percent}" 
	
sujit=stud("Sujit","singh",12,5,22,'90%','Football')

deepak=stud("Deepak","nagre",45,'15th',23,'80%','Cricket')

print("Student name\tRoll no.\tStandard\tBirthday\tPercentage\tSports")

print(sujit.student_details(),"\t\t",sujit.exam(),"\t\t",sujit.sports())
print(deepak.student_details(),"\t\t",sujit.exam(),"\t\t",sujit.sports())
