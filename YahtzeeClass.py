import random
from DiceClass import Dice
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
		print('Which cateogory would you like your score to go into?')	
		self.scorelist = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'chance', 'three-of-a-kind', 'four-of-a-kind', 'full-house', 'small-straight', 'large-straight', 'yahtzoom']
		self.choice = str(input('\n'))
		self.choice.lower()
		if self.choice == 'ones':
			countmult(1)
			self.total1 = self.total
		elif self.choice == 'twos':
			countmult(2)
			self.total2 = self.total
		elif self.choice == 'threes':
			countmult(3)
			self.total3 = self.total
		elif self.choice == 'fours':
			countmult(4)
			self.total4 = self.total
		elif self.choice == 'fives':
			countmult(5)
			self.total5 = self.total
		elif self.choice == 'sixes':
			countmult(6)
			self.total6 = self.total
		elif self.choice == 'chance':
			chance()
		elif self.choice =='three-of-a-kind':
			threefour()
			self.total = self.total8
		elif self.choice =='four-of-a-kind':
			threefour()
			self.total = self.total9
		elif self.choice == 'full-house':
			fullhouse()
		elif self.choice == 'small-straight':
			smallstraight()
		elif self.choice == 'large-straight':
			largestraight()
		elif self.choice == 'yahtzoom':
			yahtzoomprint()
		else:
			print('That is wrong')
			score()



	#All of the categories that you can score with:

	def countmult(self, number):
		self.total = self.list1.count(self.number)*self.number
	

	def chance(self):
		self.total7 = sum(self.list1)
		if sum(self.list == 17):
			self.total7 = 40

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
	def yahtzoomprint(self):
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
