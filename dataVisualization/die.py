from random import randint
class Die():
	"""class representing a die"""
	def __init__(self,num_sides=6):
		"""dice default to 6 side"""
		self.num_sides=num_sides
		
	def roll(self):
		"""return a random number between 1 and the number of dice sides"""
		return randint(1,self.num_sides)
