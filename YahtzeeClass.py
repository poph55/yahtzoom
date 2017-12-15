import random
from DiceClass import Dice
class Yahtzoom:
    def __init__(self):
    	name = 0

	def reroll(self):
		print("Enter the number of each die you would like to reroll separately. Press 0 to continue.")

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

	def score(self):
		print('Which cateogory would you like your score to go into?')
