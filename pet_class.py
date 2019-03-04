class pet:
	# animal_name=['lion','rat','elephant','bear']

	def __init__(self,name,sound):		# initial function
			self.name=name
			self.sound=sound

	def anim(self):						# userdefined function
		return f"{self.name}"

	def anim1(self):					# userdefined function
		return f"{self.sound}"		

p=pet("lion","roaring")
p1=pet("rat","squeak")
p2=pet("elephant","trumpeting")
p3=pet("bear","growling")

print(p.anim().capitalize()+" is "+p.anim1())
print(p1.anim().capitalize()+" is "+p1.anim1())
print(p2.anim().capitalize()+" is "+p2.anim1())
print(p3.anim().capitalize()+" is "+p3.anim1())