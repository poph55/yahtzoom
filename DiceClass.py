
import random
class Dice:
	def __init__(self):
		self.value = 0

	def roll(self):
		self.value = int(random.uniform(1,7))

die1 =Dice()
die1.roll()
print(die1.value)
die2 =Dice()
die2.roll()
print(die2.value)
die3 =Dice()
die3.roll()
print(die3.value)
die4 =Dice()
die4.roll()
print(die4.value)
die5 =Dice()
die5.roll()
print(die5.value)