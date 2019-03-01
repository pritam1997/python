class Car:
	modelnames = ['bmw','maruti','skoda']
	def __init__(self,name,modelyear,mileage):
		if name in Car.modelnames:
			self.name = name
		else:
			print("Name of car is not defined in accepted list.")
			# break
		self.modelyear = modelyear
		self.mileage = mileage

	def names(self):
		return f"The car name is {self.name}"

c = Car("bmw",2014,"24kmpl")
c1 = Car("skoda",2015,"24kmpl")

print(c.names())
print(c.mileage)
print(c1.names())

