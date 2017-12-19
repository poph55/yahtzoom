#Runner Class
from DiceClass import Dice
from YahtzeeClass import Yahtzoom
list1 = []
finaltotal = []
game1 = Yahtzoom(list1)
#Executing the main functions
#while len(game1.scorelist) > 0:
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
		game1.reroll()

		print(list1)

		again = str(input('Would you like to roll your dice again? Y/N  \n'))
		again = again.lower()
		while again != 'y' and again != 'n':
			print('That is not an option!')
			again = str(input('Would you like to roll your dice again? Y/N  \n'))
		if again == 'y':
			game1.reroll()
		print('Here are you final dice rolls: \n')
		print(list1)

	elif again =='n':
		print('Here are you final dice rolls: \n')
		print(list1)
	#Picking a cateogory Function
	print(game1.scorelist)
	game1.score()
	game1.choice = 'full'
	game1.totalscore()
	finaltotal.append(game1.finalscore)
	#Score Function
	#Total Sum Function
print(sum(finaltotal))
