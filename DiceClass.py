
import random
#Class for dice
class Dice:
	#constructor
	def __init__(self):
		self.value = 0

	#Rolling the dice
	def roll(self):
		self.value = int(random.uniform(1,7))


