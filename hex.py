
class Hex:
	def __init__(self, ID = None, terrain = None, features = [], lairs = [], subHex = []):
		self.ID = ID
		self.features = features
		self.lairs = lairs
		self.terrain = terrain

	def AddFeature(self, feat, num):
		self.features.append(feat)

	def AddLair(self, lair, num):
		self.lairs.append(lair)

	def GetSubHex(self, num):
		l = []
		for x in self.features:
			if x.subHex == num:
				l.append(x)
		for x in self.lairs:
			if x.subHex == num:
				l.append(x)