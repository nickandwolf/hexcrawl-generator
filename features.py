from random import randint as r
import features.features as F
import math
# MAKE SURE TO HAVE SOME THINGS REFERENCE EACH OTHER
# BREAK EACH THING INTO SUB FUNCTIONS
class Feature:
	def __init__(self, type = None, details = None):
		self.type = type
		self.details = details

	def Water(self):
		pass #TODO:roll on water table

	def Terrain(self):
		pass #TODO:roll on the terrain table

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