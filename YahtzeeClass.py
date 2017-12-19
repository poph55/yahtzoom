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

	#Special print if you get Yahtzee
	def yahtzoomprint(self):

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
		print('Which cateogory would you like your score to go into?')
		self.scorelist = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'chance', 'three of a kind', 'four of a kind', 'full house', 'small straight', 'large straight', 'yahtzoom']
		self.choice = str(input())
		

	#All of the categories that you can score with:
	def chancethreefour(self):
		self.total = sum(self.list1)

	def ones(self):
		self.total = self.list1.count(1)

	def twos(self):
		self.total = self.list1.count(2)*2

	def threes(self):
		self.total = self.list1.count(3)*3

	def fours(self):
		self.total = self.list1.count(4)*4

	def fives(self):
		self.total = self.list1.count(5)*5

	def sixes(self):
		self.total = self.list1.count(6)*6




