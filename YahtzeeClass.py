import random
from DiceClass import Dice
import sys
#Class for our game Yahtzoom
class Yahtzoom:
	def __init__(self, list1):
		self.list1 = list1
		self.scorelist = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'chance', 'three-of-a-kind', 'four-of-a-kind', 'full-house', 'small-straight', 'large-straight', 'yahtzoom']
		self.total1 = 0
		self.total2 = 0
		self.total3 = 0
		self.total4 = 0
		self.total5 = 0
		self.total6 = 0
		self.total7 = 0
		self.total8 = 0
		self.total9 = 0
		self.total10 = 0
		self.total11 = 0
		self.total12 = 0
		self.total13 = 0
		self.finalscore = 0

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

	def countmult(self, number):
		self.number = number
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
		if (self.list1[0] == self.list1[1] and self.list1[1] == self.list1[2] and self.list1[3] == self.list1[4]) or (self.list1[0] == self.list1[1] and self.list1[2] == self.list1[3] and self.list1[3] == self.list1[4]):
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


		#Scoring Function
	def score(self):
		print('Which category would you like your score to go into?')
		self.choice = str(input('\n' + str(self.scorelist) + '\n'))
		self.choice.lower()
		if self.choice == 'ones':# and self.ones1 != 'full':
			Yahtzoom.countmult(self, 1)
			self.total1 = self.total
			self.ones1 = 'full'
		elif self.choice == 'twos':# and self.twos1 != 'full':
			Yahtzoom.countmult(self, 2)
			self.total2 = self.total
			self.twos1 = 'full'
		elif self.choice == 'threes':# and self.threes1 != 'full':
			Yahtzoom.countmult(self, 3)
			self.total3 = self.total
			self.threes1 = 'full'
		elif self.choice == 'fours':# and self.fours1 != 'full':
			Yahtzoom.countmult(self, 4)
			self.total4 = self.total
			self.fours1 = 'full'
		elif self.choice == 'fives':# and self.fives1 != 'full':
			Yahtzoom.countmult(self, 5)
			self.total5 = self.total
			self.fives1 = 'full'
		elif self.choice == 'sixes':# and self.sixes1 != 'full':
			Yahtzoom.countmult(self, 6)
			self.total6 = self.total
			self.sixes1 = 'full'
		elif self.choice == 'chance':# and self.chance1 != 'full':
			Yahtzoom.chance(self)
			self.chance1 = 'full'
		elif self.choice =='three-of-a-kind':# and self.threekind != 'full':
			Yahtzoom.threefour(self)
			self.total8 = self.total
			self.threekind = 'full'
		elif self.choice =='four-of-a-kind':# and self.fourkind1 != 'full':
			Yahtzoom.threefour(self)
			self.total9 = self.total
			self.fourkind1 = 'full'
		elif self.choice == 'full-house':# and self.johnstamos != 'full':
			Yahtzoom.fullhouse(self)
			self.johnstamos = 'full'
		elif self.choice == 'small-straight':# and self.sstraight != 'full':
			Yahtzoom.smallstraight(self)
			self.sstraight = 'full'
		elif self.choice == 'large-straight':# and self.lstraight != 'full':
			Yahtzoom.largestraight(self)
			self.lstraight = 'full'
		elif self.choice == 'yahtzoom':
			Yahtzoom.yahtzoom(self)
		else:
			print('That is wrong')



	#All of the categories that you can score with:


	def totalscore(self):
		self.finalscore = self.total1 + self.total2 + self.total3 + self.total4 + self.total5 + self.total6 + self.total7 + self.total8 + self.total9 + self.total10 + self.total11 + self.total12 + self.total13
		