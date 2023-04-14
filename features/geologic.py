def Geologic(self):
	rollz1 = r(1,6)
	result = ""
	if rollz1 == 1:
		result = self.Caves()
		
	elif rollz1 == 2:
		result = self.Change_in_Elevation()
		
	elif rollz1 == 3:
		result = self.Rock()
		
	elif rollz1 == 4:
		result = self.Soil()
		
	elif rollz1 == 5:#TODO
		pass#result = self.Water()

	else:
		pass#result = self.Terrain()
		
def Caves(self):
	result = "Cave\n"
	num = ""
	roll = r(1,100)
	if roll < 11:
		num = 0
	elif roll < 51:
		num = 1
	elif roll < 76:
		num = 2
	elif roll < 91:
		num = 3
	elif roll < 100:
		num = r(1,4) + 2
	else:
		num = r(1,4) + r(1,4) + 2

	for x in range(num):
		roll = r(1,100)
		if roll < 36:
			result += "A typical entrance. "
		elif roll < 71:
			result += "A sinkhole. "
		elif roll < 86:
			result += "Naturally concealed entrance. "
		else:
			result += "Obviously worked entrance. "
	result = result.strip()
	num = 0
	roll = r(1,100) + (5*num)
	if roll < 41:
		num = 1
	elif roll < 61:
		num = r(1,4)+1
	elif roll < 81:
		num = r(1,6) + r(1,6) + r(1,6)
	elif roll < 96:
		num = r(1,12) + r(1,12) + r(1,12) + r(1,12)
	elif roll < 101:
		num = r(1,20) + r(1,20) + r(1,20) + r(1,20) + r(1,20)
	else:
		num = r(1,100) + r(1,100) + r(1,100) + r(1,100) + r(1,100) + r(1,100)
	
	result += "\nThere are " + str(num) + " chamber(s).\n"
	percy = 0 #chance of getting into Underborea
	for x in range(num):
		if x % 10 == 0:
			if r(1,6) == 1:
				result += "One chamber leads one level deeper... "
				percy += 1
			if r(1,100) <= percy:
				result += "into Underborea! "
		if r(1,3) == 1:
			roll = r(1,100)
			if roll < 66:
				result += "Two chambers are " + str((r(1,4))*100) + " yards apart."
			elif roll < 91:
				result += "Two  chambers are " + str((r(1,6) + r(1,6) + r(1,6) + r(1,6)) * 100) + " yards apart."
			else:
				result += "Two chambers are " + str(r(1,4)) + " mile(s) apart."
			result += "\n"
	
	roll = r(1,6)
	if roll < 3:
		result += "The cave is dry."
	elif roll < 5:
		result += "The cave is wet."
	elif roll < 6:
		result += "The cave is split between wet and dry sections."
	else:
		result += "The cave is unnatural (burrowed, lava tubes, magic)."
	return result

def Change_in_Elevation(self):
	result = "Change in Elevation\n"
	roll = r(1,100)
	if roll < 76:
		result += "The change is natural."
	elif roll < 91:
		result += "The change is natural but not to the area."
	elif roll < 97:
		result += "The change is from years of physical labor."
	else:
		result += "The change is the work of magic."

	result += "\n"
		
	roll = r(1,100)
	num = 0
	if roll < 51:
		num = r(1,20) + r(1,20) + r(1,20) + r(1,20) + r(1,20)
	elif roll < 76:
		num = r(1,20) + r(1,20) + r(1,20) + r(1,20) + r(1,20) + r(1,20) + r(1,20) + r(1,20) + r(1,20) + r(1,20)
	else:
		num = r(1,10) * 100

	if r(1,2) == 1:
		result += "The land is " + str(num) + " higher than the surrounding area."
	else:
		result += "The land is " + str(num) + " lower than the surrounding area."

	result += "\n"

	roll = r(1,100)
	if roll < 36:
		result += "It compromises only 1.2 miles."
	elif roll < 71:
		result += "It compromises " + str(round((r(1,4) + 1)*1.2),1) + " miles."
	elif roll < 86:
		result += "It compromises " + str(round((r(1,4) + r(1,4) + r(1,4))*1.2),1) + " miles."
	elif roll < 99:
		result += "It compromises " + str(round((r(1,8) + r(1,8) + r(1,8) + r(1,8))*1.2),1) + " miles."
	else:
		result += "It compromises " + str(round((r(1,4) + 1)*24),1) + " miles."

	if r(1,3) == 1:
		if r(1,3) == 1:
			result += "\nThe elevation is 2 degrees from the current biome."
		else:
			result += "\nThe elevation is 1 degree from the current biome."

	return result

def Rock(self):
	result = "Rocks\n"
	roll = r(1,100)
	if roll < 36:
		rad = r(1,6) - 1
		if rad == 0:
			rad = r(1,9)/10
		dens = r(1,10) + r(1,10) + r(1,10)
		per = r(1,20)*100
		per = round(math.sqrt(per))
		result += str(rad) + "ft in average diameter rocks with about " + str(dens) + " every " + str(per) + "x" + str(per) + " ft.\n"

		size = 0
		r2 = r(1,100)
		if r2 < 31:
			size = r(1,4)*100
		elif r2 < 51:
			size = (r(1,6) + r(1,6))*500
		elif r2 < 66:
			size = (r(1,8) + r(1,8) + r(1,8))*1000
		elif r2 < 81:
			size = (r(1,10) + r(1,10) + r(1,10) + r(1,10))*10000
		elif r2 < 91:
			size = r(1,4)*26074875
		elif r2 < 96:
			size = (r(1,6) + r(1,6) + r(1,6))*26074875
		elif r2 < 100:
			size = (r(1,8) + r(1,8) + r(1,8) + r(1,8))*26074875
		else:
			size = r(1,4)*10429949930
		
		size = round(math.sqrt(size))
		result += "It covers about " + str(size) + "x" + str(size) + " ft."
		
	elif roll < 71:
		rad = r(1,6) + r(1,6) + r(1,6)
		dens = r(1,4)
		per = r(1,20)*100
		result += str(rad) + " ft in average diameter rocks with about " + str(dens) + " every " + str(per) + "x" + str(per) + " ft.\n"

		size = 0
		r2 = r(1,100)
		if r2 < 31:
			size = r(1,4)*100
		elif r2 < 51:
			size = (r(1,6) + r(1,6))*500
		elif r2 < 66:
			size = (r(1,8) + r(1,8) + r(1,8))*1000
		elif r2 < 81:
			size = (r(1,10) + r(1,10) + r(1,10) + r(1,10))*10000
		elif r2 < 91:
			size = r(1,4)*26074875
		elif r2 < 96:
			size = (r(1,6) + r(1,6) + r(1,6))*26074875
		elif r2 < 100:
			size = (r(1,8) + r(1,8) + r(1,8) + r(1,8))*26074875
		else:
			size = r(1,4)*10429949930
		
		size = round(math.sqrt(size))
		result += "It covers about " + str(size) + "x" + str(size) + " ft."
		
	else:
		r2 = r(1,6)
		if r2 < 4:
			result += "A single outcropping of rock "
		elif r2  < 6:
			result += "" + str(r(1,4)) + " rock outcroppings "
		else:
			result += "A range of rock outcroppings "
		
		area = 0.0
		r2 = r(1,100)
		if r2 < 61:
			area = 1.2
		elif r2 < 90:
			area = (r(1,4) + 1)*1.2
		elif r2 < 97:
			area = (r(1,8) + r(1,8) + r(1,8))*1.2
		elif r2 < 100:
			area = 24
		else:
			area = (r(1,4) + 1)*24

		size = 0
		r2 = r(1,100)
		if r2 < 26:
			size = r(1,10)*1000
		elif r2 < 51:
			size = r(1,10)*10000
		elif r2 < 76:
			size = r(1,10)*100000
		else:
			size = r(1,10)*1000000
		size = round(math.sqrt(size))
		
		result += "about " + str(size) + " ft high and " + str(area) + " miles wide."

	result += "\n"
	roll = r(1,100)
	if roll < 61:
		result += "The rock is natural."
	elif roll < 96:
		result += "The rock is natural but not local."
	else:
		result += "The rock is completely unnatural."
		#1 in 6 something strange#
		if r(1,6) == 1:
			r00 = r(1,6)
			if r00 < 4:
				r0 = r(1,6)
				if r0 < 4:
					#Writing#
					thing = ""
					r2 = r(1,6)
					if r2 < 3:
						thing = "carved into "
					elif r2 < 5:
						thing = "written with chalk or paint on "
					elif r2 < 6:
						thing = "spelled out by lichen or moss on "
					else:
						thing = "organically impressed onto "

					rox = ""
					roxez
					r2 = r(1,6)
					if r2 < 4:
						rox = "a single stone."
						roxez = 1
					elif r2 < 6:
						roxez = r(1,20)+1
						rox = str(roxez) + " stones."
					else:
						rox = "all of the stones."
						roxez = float("inf")

					bleh = ""
					note = ""
					r2 = r(1,6)
					if r2 == 1:
						r3 = r(1,3)
						if r3 == 1:
							bleh = "A Meaningless phrase is "
						elif r3 == 2:
							bleh = "Obscene words are "
						else:
							bleh = "Pornographic images are "
						
					elif r2 == 2:
						if r(1,2) == 1:
							bleh = "A formula for a spell is "
						else:
							bleh = "A formula for a magic item is "

						note += "\nIt will take " + str(r(1,8)) + " weeks and " + str(roxez) + " days to decypher."
					elif r2 == 3:
						if r(1,2) == 1:
							bleh = "A prophecy of what's to come is "
						else:
							bleh = "A prophecy of what has passed is "
						if r(1,3) == 1:
							note = "\nThe prophecy is false."
					elif r2 == 4:
						r3 = r(1,6)
						if r3 < 3:
							bleh = "A treasure map is " #TODO:Roll on scrolls table for treasure
						elif r3 < 5:
							bleh = "A map of the surrounding area is "
						elif r3 == 5:
							bleh = "A map of an unknown area is "
							if r(1,2) == 1:
								note = "\nIt is to another plane."
						else:
							bleh = "A map of a random location is "
					elif r2 == 5:
						bleh = "A small crevice is "
						note = "\nIf a question is written on a slip of paper and left, the next day the paper will hold an answer."
						r3 = r(1,3)
						if r3 == 1:
							note += "\nIt must be written in a specific language."
						elif r3 == 2:
							note += "\nIt is written in the user's blood."
						else:
							note += "\nIt is accompanied with a gift."

						r3 = r(1,6)
						if r3 < 4:
							note += "\nTreat the answer as an Augury "
						elif r3 < 6:
							note += "\nTreat the answer as a Divination "
						else:
							note += "\nTreat the answer as a Commune "
						note += "cast from a " + str((r(1,8)+4)) + " level Cleric."
					else:
						r3 = r(1,5) #6 is referee's choosing
						if r3 == 1:
							bleh = "A record of historical events are "
						elif r3 == 2:
							bleh = "A warning of "
							r4 = r(1,6)
							if r4 < 5:
								bleh += "current dangers are "
							else:
								bleh += "past dangers are "
						elif r3 == 3:
							bleh = "A letter to one of the adventurers is "
							if r(1,2) == 1:
								note = "\n It is from a dead relative or friend."
							if r(1,3) == 1:
								note += " It gives advice on a future event."
							else:
								note += " It is just a friendly hello."
						elif r3 == 4:
							bleh = "A random letter is "
							r4 = r(1,6)
							note = "\nWhen arrange the letters spell out "
							if r4 < 3:
								note += "a dirty word."
							elif r4 < 5:
								note += "the name of a ancient king or sorcerer."
							elif r4 < 6:
								note += "the name of a party member who will betray them."
							else:
								note += "the true name of a daemon."
						elif r3 == 5:
							bleh = "Assembly directions are "
							r4 = r(1,6)
							if r4 < 3:
								note = "\nIt will create a sculpture."
							elif r4 < 5:
								note = "\nIt will create a crude dwelling."
							elif r4 < 6:
								note = "\nIt will create a portal to another world."
								r5 = r(1,6)
								if r5 == 1:
									note += "\nIt can be used " + str(r(1,4)) + " times."
								elif r5 == 2:
									note += "\nIt lasts " + str(r(1,4)) + " hours."
								elif r5 == 3:
									note += "\nIt lasts " + str(r(1,4)+r(1,4)+r(1,4)) + " hours."
								elif r5 == 4:
									note += "\nIt lasts " + str(r(1,4)) + " days."
								elif r5 == 5:
									note += "\nIt lasts " + str(r(1,4)) + " weeks."
								else:
									note += "\nIt is permanent."
							else:
								note = "\nA circle " + str(r(1,20)+10) + "ft in diameter which protects the party from wandering monsters."
								r5 = r(1,6)
								if r5 == 1:
									note += "\nIt can be used " + str(r(1,4)) + " times."
								elif r5 == 2:
									note += "\nIt lasts " + str(r(1,4)) + " hours."
								elif r5 == 3:
									note += "\nIt lasts " + str(r(1,4)+r(1,4)+r(1,4)) + " hours."
								elif r5 == 4:
									note += "\nIt lasts " + str(r(1,4)) + " days."
								elif r5 == 5:
									note += "\nIt lasts " + str(r(1,4)) + " weeks."
								else:
									note += "\nIt is permanent."

					result += bleh + thing + rox + note
			
			if r00 < 6:
				##PATTERN
				if r(1,3) == 1:
					view = "from above."
				else: view = "from ground level."
				r0 = r(1,3)
				if r0 == 1:
					view = ""
				elif r0 == 2:
					view = "\nIt forms a nundane shape when viewed " + view
				else:
					view = "\nForms a magical pattern when viewed " + view + "\nIt takes " + str(r(1,8)) + " days of study to determine it's purpose."
					r69 = r(1,6)
					if r69 == 1:
						view += "\nIt wards against something." #TODO:roll on scrolls to determine ward
					elif r69 == 2:
						rrr = r(1,6)
						if rrr < 4:
							view += "\nIt serves as a portal to point in this world."
						elif rrr < 6:
							view += "\nIt serves as a portal to another world."
						else:
							view += "\nIt serves as a portal to another time period."
					elif r69 == 3:
						rrr = r(1,3)
						if rrr == 1:
							view += "\nIt moderates the local weather."
						elif rrr == 2:
							view += "\nIt intensifies the local weather."
						else:
							view += "\nIt attracts a certain weather phenomenon."
					elif r69 == 4:
						view += "\nIt is a prison for " + str(r(1,10)) + "HD of creature(s)."
					elif r69 == 5:
						view += "\nIt is a focal point for a ley line." #TODO:roll magic and hex 13.22
						if r(1,2) == 1:
							view += "\nThe ley line has since moved."
					else:
						view += "\nIt is an artifact designed to cast a permanent spell over a larger area."
					result += view
			else:
				##MAGICAL
				pass #TODO: roll on magic features section

	return result

def Soil(self):
	result = "Soil\n"
	if r(1,3) == 1:
		result += "The soil looks like surrounding soil."
	else:
		if r(1,6) == 1:
			result += "The soil appears unnatural."
		else: result += "The soil appears different than the surrounding soil."

	roll = r(1,3)
	if roll == 1:
		result += "\nIt is as productive as the surrounding soil."
	elif roll == 2:
		result += "\nIt is more productive than the surrounding soil."
	else:
		result += "\nIt is less productive than the surrounding soil."

	roll = r(1,6)
	if roll < 4:
		result += "\nThis is caused by a naturally occuring feature. (minerals, nutrients, etc.)"
	elif roll < 6:
		result += "\nThis is caused by an artificial means. (terraced, fertalized, poisoned, etc.)\nIt will cost 1000gp per subhex to alter the soil."
	else:
		result += "\nThis is caused by a curse or beneficial spell. It is possible to remove the magic."
