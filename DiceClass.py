
import random
class Dice:
	def __init__(self):
		self.value = 0

	def roll(self):
		self.value = int(random.uniform(1,7))


