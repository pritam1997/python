def a(s):
	print(s)
a("asd")

# function with argument 

def arg(arg):
	print(arg)

arg("This is argument")

#function with keyword argument 

def kwd(first, second):					#parameter
	return f"{first} {second}"

print(kwd (first="key",second="word"))	#keyword argument

#function with Default argument

def defarg(name="python", age=20):		# Default Argument
	return f"{name} {age}"

print(defarg(name="abcd"))


#function with variable-length argument

def fun(arg,a,*kwd):
	print(arg,a)
	s=0
	for i in kwd:
		s=s+i
	return s

fun(234,23676)		# both argument passing in 1st 2 parameters

print(fun(1,2,3,4,5,6,7,8,9,10))		# both argument passing in 1st 2 parameters and 3rd argument passing in 3rd parameter

def f(**kwd):
	for k,v in kwd.items():
		print(k,v)

f(one=1,two=2)