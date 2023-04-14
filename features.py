from random import randint as r
import math
# MAKE SURE TO HAVE SOME THINGS REFERENCE EACH OTHER
# BREAK EACH THING INTO SUB FUNCTIONS
class Feature:
	def __init__(self, type = None, details = None):
		self.type = type
		self.details = details

	def Geologic(self):
		rollz1 = r(1,6)
		result = ""
		if rollz1 == 1:
			result = self.G_Caves()
			
		elif rollz1 == 2:
			result = self.G_Change_in_Elevation()
			
		elif rollz1 == 3:
			result = self.G_Rock()
			
		elif rollz1 == 4:
			result = self.G_Soil()
			
		elif rollz1 == 5:
			result = self.Water()

		else:
			result = self.Terrain()
		
	def G_Caves(self):
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

	def G_Change_in_Elevation(self):
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

	def G_Rock(self):
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

	def G_Soil(self):
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

	def Water(self):
		pass #TODO:roll on water table

	def Terrain(self):
		pass #TODO:roll on the terrain table

	def Structure(self):
		result = ""
		roll = r(1,10)
		if roll == 1:
			self.S_Burial_Grounds()
			
		elif roll == 2:
			self.S_Monuments()
			
		elif roll < 6:
			self.S_Dwellings()
			
		elif roll == 6:
			self.S_Fortifications()
			
		elif roll < 9:
			self.S_Infrastructure()
			
		elif roll == 9:
			self.S_Barriers()
			
		else:
			self.S_Dungeons()

		return result

	def S_Burial_Grounds(self):
		result = "Burial Grounds\n"
		roll = r(1,100)

		if roll < 31:
			result += "A single dead body "
			ded = 1
		elif roll < 61:
			ded = r(1,4) + 1
			result += "" + str(ded) + " dead "
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

		perm = False #permanent markers
		rel = False #religious affiliation
		roll = r(1,100)

		if roll < 26:
			result += "left exposed to the elements."
		elif roll < 31:
			result += "buried in a mass grave."
		elif roll < 61:
			result += "buried with wooden markers."
			rel = True
			perm = True
		elif roll < 76:
			result += "buried with tombstones."
			rel = True
			perm = True
		elif roll < 81:
			result += "buried in mausoleums or crypts."
			rel = True
			perm = True
		elif roll < 87:
			result += "buried in barrows or burial mounds."
			rel = True
			perm = True
		elif roll < 91:
			result += "ritually exposed to the elements."
			rel = True
		elif roll < 96:
			result += "executed as punishment. (gibbets, crucifixion, gallows, etc.)"
			perm = True
		elif roll < 100:
			result += "buried in unmarked graves."
		else:
			result += "killed by magic. (turned to stone or trees, frozen in ice, embedded in amber, etc.)"
		
		result += "\n"
		if r(1,2) == 1 and perm:
			result += "The grave is marked "
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
				
			roll = r(1,10)
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
		roll = r(1,100)
		if roll < 6:
			age = r(1,4)
			result += "They appear to be " + str(age) + " days old."
		elif roll < 11:
			age = r(1,4)
			result += "They appear to be " + str(age) + " weeks old."
		elif roll < 21:
			age = r(1,12)
			result += "They appear to be " + str(age) + " months old."
		elif roll < 31:
			age = r(1,10)
			result += "They appear to be " + str(age) + " years old."
		elif roll < 41:
			age = r(1,20) + r(1,20)
			result += "They appear to be " + str(age) + " years old."
		elif roll < 51:
			age = 0
			for x in range(5):
				age += r(1,20)
			result += "They appear to be " + str(age) + " years old."
		elif roll < 76:
			age = 0
			for x in range(10):
				age += r(1,20)
			result += "They appear to be " + str(age) + " years old."
		elif roll < 100:
			age = 0
			for x in range(10):
				age += r(1,100)
			result += "They appear to be " + str(age) + " years old."
		else:
			age = r(1,4)
			result += "They appear to be " + str(age) + " millennia old."
		result += "\n"
		roll = r(1,100)
		if roll < 51:
			result += "They appear to be human." #TODO:Roll hyperborean races
		elif roll < 76:
			result += "They appear to be human." #TODO:Roll rare hyperborean races
		elif roll < 91:
			result += "They appear to be humanoid." #TODO:Roll the reincarnation table
		elif roll < 96:
			result += "They appear to be monsters." #TODO:Roll it!
		else:
			result += "They appear to be a mix of various races, humanoids, and monsters." #TODO: Roll it!
		chances = 3
		if rel:
			chances += 1
		if r(1,6) <= chances:
			result += "The bodies appear to have been buried as part of a religious ceremony.\n"
			test = round(ded/50)
			if r(1,6) <= test:
				result += "The ground is unhallowed:\n"
				def lilDedBuddies(ro):
					li = ["The dead walk.","The dead resist.","The dead persist.","The dead protest.","The evil permeates.","The dead hunger.","The dead corrupt.","The dead speak."] #the initial thing.
					lo = []
					for x in range(ro):
						rill = r(1,len(li))-1
						tex = "\n" #added details
						if rill == 0:
							tex += "Those that die within have a 1:6 chance of rising as a "
							rille = r(1,6)
							if rille < 4:
								tex += "skeleton "
							elif rille < 6:
								tex += "zombie "
							else:
								tex += "ghoul "
							tex += "every night while within the gravesite.\n"
						elif rill == 1:
							tex += "Undead have +"
							rille = r(1,6)
							if rille < 4:
								tex += "1"
							elif rille < 6:
								tex += "2"
							else:
								tex += "3"
							tex += "HD for turning purposes."
							
						elif rill == 2:
							tex += "Undead use a d10 instead of a d8 for HP"
							if r(1,3) == 1:
								rille = r(1,4)
								if rille == 1:
									tex += " and regenerate 1HP per round while within the gravesite."
								elif rille == 2:
									tex += " and return to 1HP the first time they are reduced to 0HP."
								elif rille == 3:
									tex += " and will reform in 1d6 "
									rioil = r(1,6)
									if rioil == 1:
										tex += "rounds"
									elif rioil < 4:
										tex += "minutes"
									elif rioil < 6:
										tex += "hours"
									else:
										tex += "days"
									tex += " unless burned, blessed by a cleric, or removed from the gravesite."
								else:
									tex += " and have +"
									rioil = r(1,6)
									if rioil < 4:
										tex += "1 AC."
									elif rioil < 6:
										tex += "2 AC."
									else:
										tex += "3 AC."
						elif rill == 3:
							tex += "Natural and magical healing is stifled. No natural healing occurs and magical healing rolls twice and take the worst roll."
						elif rill == 4:
							tex += "The entire area radiates evil. Detecting alignment do not work as do weapons requiring alignment.\nLawful and Good characters take a -1 to surprise and have difficulty sleeping. Must Save vs Spell or fail to rest."
						elif rill == 5:
							tex += "Undead creatures crit on a 19 or 20. Lawful and Good characters roll saving throws twice and take the worst roll."
						elif rill == 6:
							tex += "Magic items have a 2:6 chance of becoming cursed if left in the gravesite for more than a week."
						else:
							tex += "Voices of the dead fill the air. Good and Lawful characters suffer a -1 to initiative and surprise.\nThey must also Save vs Spell each time they enter or be affect with Blight or Confusion spells."
						
						lo.append(li.pop(rill) + tex + "\n")
					
					return lo
				roll = r(1,3)
				bleh = lilDedBuddies(roll)
				for b in bleh:
					result += b
			
		return result

	def S_Monuments(self):
		result = "Monuments\n"
		notes = ""
		roll = r(1,100)
		if roll < 26:#statues
			plural = False #more than one?
			if r(1,6) < 5:
				plural = True
			r1 = r(1,100)
			if r1 < 41:
				if plural:#TODO: Roll hyperborean races
					result += "A statue of a human "
				else:
					result += "Multiple statues of humans "
			elif r1 < 76:
				if plural:#TODO: Roll rare hyperborean races
					result += "A statue of a human "
				else:
					result += "Multiple statues of humans "
			elif r1 < 91:
				if plural:#TODO: Roll on hyperborean reincarnation
					result += "A statue of a humanoid "
				else:
					result += "Multiple statues of humanoids "
			elif r1 < 99:
				if plural:#TODO: Roll monsters of the area
					result += "A statue of a monster "
				else:
					result += "Multiple statues of monsters "
			else:
				if plural:#TODO: Roll something?
					result += "A statue of some abstract concept "
				else:
					result += "Multiple statues of some abstract concepts "

			if r(1,100) == 1:
				results += "(made by petrification) "
				if r(1,3) == 1:
					notes += "There is treasure which can be recovered if unpetrified.\n"
				
		elif roll < 51:#obelisk
			if r(1,2) == 1:
				result += "An obelisk "
			else:
				if r(1,3) == 1:
					result += "A cluster of " + str(r(1,8)+1) + " columns "
				else:
					result += "A column "
		elif roll < 76:#megalith
			result += "A megalith "
		elif roll < 86:#freeform
			r1 = r(1,3)
			if r1 == 1:
				result += "An arch "
			elif r1 == 2:
				result += "A building "
			else:
				result += "A freeform structure "
		elif roll < 91:#pyramid
			r1 = r(1,3)
			if r1 == 1:
				result += "A pyramid "
			elif r1 == 2:
				result += "A terraced pyramid "
			else:
				r2 = r(1,3)
				if r2 == 1:
					result += "A roughly pyramid shaped "
				elif r2 == 2:
					result += "A geometrically shaped " #TODO: Roll it!
				else:
					result += "An abstractly shaped "
				result += "earthen mound "
		elif roll < 96:#fountain
			pass #TODO: ROLL IT!
		else:#magical
			pass #TODO: ROLL IT!
		
		#built for...
		roll = r(1,100)
		if roll < 26: #honor the dead
			result += "built to honor the dead."
		elif roll < 51: #honor an event
			result += "built to honor an event."
		elif roll < 76: #honor an individual
			result += "built to honor a person."
		elif roll < 86: #honor a concept
			result += "built to honor an alignment." #TODO: Roll it!
		elif roll < 96: #honor a diety
			result += "built to honor a diety." #TODO: Roll it!
		else: #built to house an artifact/relic or individual
			result += "built to house a relic or individual." #TODO: Roll it!

		result += "\n"
		roll = r(1,6)
		if roll == 1:
			result += "The features have been completely worn away by "
		elif roll == 2:
			result += "The features have been worn away by "
		elif roll == 3:
			result += "The features are lightly weathered by "
		else:
			result += "The features are clear despite "

		if r(1,2) == 1:
			result += "natural erosion."
		else:
			result += "vandalism."
		
		result += notes + "\n"
		result += "It appears to have been made by "
		
		roll = r(1,100) #TODO: Add rolling to it
		if roll == 1:
			result += "a smaller race."
		elif roll < 61:
			result += "man."
		elif roll < 91:
			result += "a larger race."
		elif roll < 100:
		else:
		
		return result
	
	def S_Dwellings(self):
		asdf

	def S_Fortifications(self):
		asdf

	def S_Infrastructure(self):
		asdf

	def S_Barriers(self):
		asdf

	def S_Dungeons(self):
		asdf

	def Resource(self):
		pass

	def Hazard(self):
		pass

	def Sign(self):
		pass

	def Dungeon(self):
		pass

	def Terrain(self):
		pass

	def Settlement(self):
		pass

	def Water(self):
		pass

	def Magic(self):
		pass