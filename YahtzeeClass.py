import random
from DiceClass import Dice
import sys
#Class for our game Yahtzoom
class Yahtzoom:
	def __init__(self, list1):
		self.list1 = list1

	#Function that selects which one that you want to rhttp://collabedit.com/eroll
	def reroll(self):
		rollagain = []
		while 1==1:
			rerollinput = int(input("What dice would you like to reroll?"))
			while rerollinput != 1 and rerollinput != 2 and rerollinput !=3 and rerollinput != 4 and rerollinput != 5 and rerollinput != 6:
				while rerollinput != 0:
					try:
						rerollinput = int(input("What dice would you like to reroll?"))
						break
					except:
						print("That ain't valid you yellow-bellied sap sucker.")
				if rerollinput == 0:
					break
			if rerollinput == 0:
				break
			rollagain.append(rerollinput)
		die6 = Dice()
		clock = len(rollagain)
		while clock > 0:
			clock -= 1
			die6.roll()
			self.list1[rollagain[clock-1]-1] = die6.value



		#Scoring Function
	def score(self):
		print('Which category would you like your score to go into?')
		self.choice = str(input('\n'))
		self.choice.lower()
		if self.choice == 'ones' and self.ones != 'full':
			countmult(1)
			self.total1 = self.total
			self.ones = 'full'
		elif self.choice == 'twos' and self.twos != 'full':
			countmult(2)
			self.total2 = self.total
			self.twos = 'full'
		elif self.choice == 'threes' and self.threes != 'full':
			countmult(3)
			self.total3 = self.total
			self.threes = 'full'
		elif self.choice == 'fours' and self.fours != 'full':
			countmult(4)
			self.total4 = self.total
			self.fours = 'full'
		elif self.choice == 'fives' and self.fives != 'full':
			countmult(5)
			self.total5 = self.total
			self.fives = 'full'
		elif self.choice == 'sixes' and self.sixes != 'full':
			countmult(6)
			self.total6 = self.total
			self.sixes = 'full'
		elif self.choice == 'chance' and self.chance != 'full':
			chance()
			self.chance = 'full'
		elif self.choice =='three-of-a-kind' and self.threekind != 'full':
			threefour()
			self.total = self.total8
			self.threekind = 'full'
		elif self.choice =='four-of-a-kind' and self.fourkind != 'full':
			threefour()
			self.total = self.total9
			self.fourkind = 'full'
		elif self.choice == 'full-house' and self.johnstamos != 'full':
			fullhouse()
			self.johnstamos = 'full'
		elif self.choice == 'small-straight' and self.sstraight != 'full':
			smallstraight()
			self.sstraight = 'full'
		elif self.choice == 'large-straight' and self.lstraight != 'full':
			largestraight()
			self.lstraight = 'full'
		elif self.choice == 'yahtzoom':
			yahtzoom()
		else:
			print('That is wrong')
			score()



	#All of the categories that you can score with:

	def countmult(self, number):
		self.total = self.list1.count(self.number)*self.number
	

	def chance(self):
		if sum(self.list == 17):
			self.total7 = 40
		else:
			self.total7 = sum(self.list1)

	def threefour(self):
		self.total = sum(self.list1)

	def fullhouse(self):
		self.list1.sort()
		if (die1.value == die2.value and die2.value == die3.value and die4.value == die5.value) or (die1.value == die2.value and die3.value == die4.value and die4.value == die5.value):
			self.total10 = 25
		else:
			self.total10 = 0

	def smallstraight(self):
		self.list1 = list(set(self.list1))
		if (self.list1[0] == self.list1[1]-1 and self.list1[1] == self.list1[2]-1 and self.list1[2] == self.list1[3]-1) or (self.list1[1] == self.list1[2]-1 and self.list1[2] == self.list1[3]-1 and self.list1[3] == self.list1[4]-1):
			self.total11 = 30
		else:
			self.total11 = 0

	def largestraight(self):
		self.list.sort()
		if (self.list1[0] == self.list1[1]-1 and self.list1[1] == self.list1[2]-1 and self.list1[2] == self.list1[3]-1 and self.list1[3] == self.list1[4]-1):
			self.total12 = 40
		else:
			self.total12 = 0


	#Special print if you get Yahtzee
	def yahtzoom(self):
		if (die1.value == die2.value and die2.value == die3.value and die3.value == die4.value and die4.value == die5.value):
			self.total13 += 50

		print("▓██   ██▓ ▄▄▄       ██░ ██ ▄▄▄█████▓▒███████▒ ▒█████   ▒█████   ███▄ ▄███▓")
		print(" ▒██  ██▒▒████▄    ▓██░ ██▒▓  ██▒ ▓▒▒ ▒ ▒ ▄▀░▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒")
		print("  ▒██ ██░▒██  ▀█▄  ▒██▀▀██░▒ ▓██░ ▒░░ ▒ ▄▀▒░ ▒██░  ██▒▒██░  ██▒▓██    ▓██░")
		print("  ░ ▐██▓░░██▄▄▄▄██ ░▓█ ░██ ░ ▓██▓ ░   ▄▀▒   ░▒██   ██░▒██   ██░▒██    ▒██ ")
		print("  ░ ██▒▓░ ▓█   ▓██▒░▓█▒░██▓  ▒██▒ ░ ▒███████▒░ ████▓▒░░ ████▓▒░▒██▒   ░██▒")
		print("   ██▒▒▒  ▒▒   ▓▒█░ ▒ ░░▒░▒  ▒ ░░   ░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░")
		print(" ▓██ ░▒░   ▒   ▒▒ ░ ▒ ░▒░ ░    ░    ░░▒ ▒ ░ ▒  ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░")
		print(" ▒ ▒ ░░    ░   ▒    ░  ░░ ░  ░      ░ ░ ░ ░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░   ")
		print(" ░ ░           ░  ░ ░  ░  ░           ░ ░        ░ ░      ░ ░         ░   ")
		print(" ░ ░                                ░                                     ")
