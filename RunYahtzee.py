#Runner Class
from DiceClass import Dice
from YahtzeeClass import Yahtzoom
import sys
list1 = []
finaltotal = []
game1 = Yahtzoom(list1)
list3 = ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'chance', 'three-of-a-kind', 'four-of-a-kind', 'full-house', 'small-straight', 'large-straight', 'yahtzoom']
print('This is YAHTZOOM!!!! Our better version of Yahtzee>\n')
print('Here are the Instructons:\n')
print('The objective of the game is to score as many points as possible.\n')
print('The game will automatically roll five dice for you. You then have the option to re-roll the dice by printing Y or N\n')
print('In order to re-roll, you have to enter which die to re-roll by its place in the list, NOT by its value.\n')
print('You also have to only enter the die one at a time. The game will then ask you the same question again where you will enter a different die.\n')
print('When you have entered all of the dice that you want to re-roll, then enter 0 to continue.\n')
print('You only get to roll the dice 3 times per turn and you get 13 turns per game.\n')
print('Each turn you must also pick the category that you want your score to go into. You can only choose each category once.\n')
print('Categories:  ' + str(list3))
input('\nWhen you are ready to start, press enter.')


#Executing the main functions
sys.os('clear')
for x in range(0,13):
	list1 = []
	die1 =Dice()
	die1.roll()
	list1.append(die1.value)
	die2 =Dice()
	die2.roll()
	list1.append(die2.value)
	die3 =Dice()
	die3.roll()
	list1.append(die3.value)
	die4 =Dice()
	die4.roll()
	list1.append(die4.value)
	die5 =Dice()
	die5.roll()
	list1.append(die5.value)

	print(list1)

	#Roll Again Function(Run twice)
	again = str(input('\nWould you like to roll your dice again? Y/N  \n'))
	again = again.lower()
	while again != 'y' and again != 'n':
		print('That is not an option!')
		again = str(input('Would you like to roll your dice again? Y/N  \n'))
	if again == 'y':
		game1.reroll(list1)

		print(list1)

		again = str(input('Would you like to roll your dice again? Y/N  \n'))
		again = again.lower()
		while again != 'y' and again != 'n':
			print('That is not an option!')
			again = str(input('Would you like to roll your dice again? Y/N  \n'))
		if again == 'y':
			game1.reroll(list1)
		sys.os('clear')
		print('Here are you final dice rolls: \n')
		print(list1)

	elif again =='n':
		sys.os('clear')
		print('Here are you final dice rolls: \n')
		print(list1)
	#Picking a cateogory Function
	game1.score()
	game1.choice = 'full'
	game1.totalscore()
	finaltotal.append(game1.finalscore)
	#Score Function
	#Total Sum Function
print(sum(finaltotal))
