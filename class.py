#class creation

class user:
	user_list = 0
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		user.user_list += 1

	def logout(self):
		user.user_list -= 1
		return user.user_list

	def full_name(self):
		active_user()
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0].upper()}.{self.last[0].upper()}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def bday(self):
		self.age += 1
		return f"Happy {self.age}th bday {self.first}"

	def active_user(self):
		return user.user_list()

user1 = user("Joe","Dane",45)
c = user.user_list
print(c)
user2 = user("Blanca","Lopez",34)
c = user.user_list
print(c)
user3 = user("Pritam", "Vishwakarma", 24)
c = user.user_list
print(c)

user1.logout()
user2.logout()

d = user.user_list
print(d)



# print(user1.full_name())
# print(user2.full_name())

# print(user1.initials())
# print(user2.initials())

# print(user1.likes("ice-cream"))
# print(user2.likes("coffee"))

# print(user1.bday())
# print(user2.bday())

# print(type(u))