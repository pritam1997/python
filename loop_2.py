for l in range(1,6):
	for a in range(1,2):
		for b in range(2,3):
			for c in range(3,4):
				for d in range(4,5):
					for e in range(5,6):
						if l==2 or l==4:
							print(f"{a} {b}   {d} {e}")
						elif l==3:
							print(f"{a}       {e}")
						else:
							print(f"{a} {b} {c} {d} {e}")