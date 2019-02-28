g=12		#global variable

def glb():	
	a=1				# now inside the function variable become local
	global g 		# this global is treat that I am global variable
	g+=1			# now variable become global
	print(a+g)
	
	def locl():
		print(g)		# printing global variable
		nonlocal a 		# now variable is nonlocal
		a+=1
		print(a)
	locl()
glb()