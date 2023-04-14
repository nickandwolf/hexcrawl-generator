from random import randint as r

def S_Burial_Grounds():
		result = "Burial Grounds\n"
		roll = r(1,100)

		if roll < 31:
			result += "A single dead body "
		elif roll < 61:
			result += "" + str(r(1,4)+1) + " dead "
		elif roll < 76:
			ded = r(1,4) + r(1,4) + r(1,4)
			result += "" + str(ded) + " dead "
		elif roll < 86:
			ded = 0
			for x in range(4):
				ded += r(1,6)
			result += "" + str(ded) + " dead "
		elif roll < 97:
			ded = 0
			for x in range(5):
				ded += r(1,10)
			result += "" + str(ded) + " dead "
		elif roll < 98:
			ded = 0
			for x in range(6):
				ded += r(1,20)
			result += "" + str(ded) + " dead "
		elif roll == 98:
			ded = 0
			for x in range(7):
				ded += r(1,100)
			result += "" + str(ded) + " dead "
		elif roll == 99:
			ded = 0
			for x in range(10):
				ded += r(1,100)
			result += "" + str(ded) + " dead "
		else:
			ded = 0
			for x in range(100):
				ded += r(1,100)
			result += "" + str(ded) + " dead "

		perm = False
		roll = r(1,100)
		if roll < 26:
			result += "left exposed to the elements."
		elif roll < 31:
			result += "buried in a mass grave."
		elif roll < 61:
			result += "buried with wooden markers."
			perm = True
		elif roll < 76:
			result += "buried with tombstones."
			perm = True
		elif roll < 81:
			result += "buried in mausoleums or crypts."
			perm = True
		elif roll < 87:
			result += "buried in barrows or burial mounds."
			perm = True
		elif roll < 91:
			result += "ritually exposed to the elements."
		elif roll < 96:
			result += "executed as punishment. (gibbets, crucifixion, gallows, etc.)"
			perm = True
		elif roll < 100:
			result += "buried in unmarked graves."
		else:
			result += "killed by magic. (turned to stone or trees, frozen in ice, embedded in amber, etc.)"
		
		if 1:
		#if r(1,2) == 1 and perm:
			result += "\nThe grave is marked "
			def lilDeth():
				roll = r(1,6)
				if roll < 3:
					return "by who is buried"
				elif roll < 5:
					return "with their birth and death date"
				elif roll == 5:
					return "with how they died"
				else:
					return "with a fact about them"
				
			roll = r(7,10)
			if roll < 7:
				result += lilDeth()
			elif roll == 7:
				result += lilDeth()
				r0 = lilDeth()
				while r0 in result:
					r0 = lilDeth()
				result += "and " + r0
			elif roll == 8:
				result += lilDeth()
				r0 = lilDeth()
				while r0 in result:
					r0 = lilDeth()
				result += ", " + r0
				r0 = lilDeth()
				while r0 in result:
					r0 = lilDeth()
				result += ", and " + r0
			else:
				result += "but it is illegible."
			result += "\n"

		return result