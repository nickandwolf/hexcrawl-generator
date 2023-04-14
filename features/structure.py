def Structure(self):
	result = ""
	roll = r(1,10)
	if roll == 1:
		self.Burial_Grounds()
		
	elif roll == 2:
		self.Monuments()
		
	elif roll < 6:
		self.Dwellings()
		
	elif roll == 6:
		self.Fortifications()
		
	elif roll < 9:
		self.Infrastructure()
		
	elif roll == 9:
		self.Barriers()
		
	else:
		self.Dungeons()

	return result

def Burial_Grounds(self):
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

def Monuments(self):
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
		result += "a giant race."
	else:
		if r(1,6) == 1:
			result += "an enormous race."
		else:
			result += "a large kingdom or empire."

	if r(1,6) == 1:
		result += "\nThere is an entrance. "
		roll = r(1,4)
		#roll 1 = visible
		if roll == 2:
			result += "It is locked."
		elif roll == 3:
			result += "It is concealed."
		elif roll == 4:
			result += "It is concealed and locked."

		result += " There are " + str(r(1,4)) + " chambers inside."

		#TODO: Use dungeon stocking table for monsters and treasure
	result += "\nIt appears to be "
	roll = r(1,100)
	if roll < 11:
		result += "" + str(r(1,10))
	elif roll < 51:
		age = 0
		for x in range(10):
			age += r(1,10)
		result += "" + str(age)
	elif roll< 96:
		age = 0
		for x in range(10):
			age += r(1,100)
		result += "" + str(age)
	else:
		age = 0
		for x in range(10):
			age += r(1,1000)
		result += "" + str(age)
	result += " years old."

	result += "\nIt is made of "
	roll = r(1,100)
	if roll < 21:
		r1 = r(1,3)
		if r1 == 1:
			result += "wood."
		elif r1 == 2:
			result += "bone."
		else:
			result += "brick."
	elif roll < 46:
		result += "metal."
	elif roll < 95:
		result += "stone."
	else:
		result += "exotic materials." #TODO: ROLL IT!

	if r(1,3) == 1:
		result += "\nIt appears to have something engraved on it..."
		if r(1,3) == 1:
			result += "however it is in a dead language"
		if r(1,3) == 1:
			result += "and was obscured by the elements" #TODO: Roll erosion vs something else
		result += "."

	if r(1,20) == 1:
		result += "\n"
		roll = r(1,6)
		if roll == 1:
			result += "This monument provides clues to a mystery. (buried treasure, a dungeon, etc.)" #TODO: ROLL IT!
		elif roll == 2:
			result += "This monument radiates magical energy and is the focal point for a randomly determined spell. It must be destroyed to stop the magic." #TODO: ROLL IT!
		elif roll == 3:
			result += "This monument is meant to capture ley line energy"
			if r(1,3) == 1:
				result += ", they ley line has since moved."
			else:
				result += "."
		elif roll == 4:
			result += "This monument serves as a prison for a powerful being." #TODO: Roll it
		elif roll == 5:
			result += "If this monument is touched, it will provide "
			if r(1,2) == 1:
				result += "a boon"
				if r(1,3) == 1:
					result += " which requires a sacrifice of some sort" #TODO: ROLL IT!
			else:
				result += "a bane"
			result += "."
		else:
			result += "This monument is actually a portal to another plane." #TODO: ROLL IT!
			if r(1,3) != 1:
				result += " It requires a ritual or spell to function." #TODO: ROLL IT!
	
	return result

def Dwellings(self):
	result = "Dwelling\n"
	
	#age
	result += "It appears to be "
	roll = r(1,100)
	if roll < 11:
		result += "" + str(r(1,10))
	elif roll < 61:
		age = 0
		for x in range(10):
			age += r(1,10)
		result += "" + str(age)
	elif roll < 100:
		age = 0
		for x in range(10):
			age += r(1,100)
		result += "" + str(age)
	else:
		age = 0
		for x in range(10):
			age += r(1,1000)
		result += "" + str(age)
	result += " years old."
	
	roll = r(1,100) #inhabited
	if roll < 26:
		asdf
	elif roll < 61:
		asdf
	else:
		adsf

def Fortifications(self):
	asdf

def Infrastructure(self):
	asdf

def Barriers(self):
	asdf

def Dungeons(self):
	asdf