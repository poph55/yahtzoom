#Runner Class
from DiceClass import Dice
from YahtzeeClass import Yahtzoom

#Executing the main functions
list1= []
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
reroll1 = Yahtzoom(list1)
again = str(input('\nWould you like to roll your dice again? Y/N  \n'))
again = again.lower()
while again != 'y' and again != 'n':
	print('That is not an option!')
	again = str(input('Would you like to roll your dice again? Y/N  \n'))
if again == 'y':
	reroll1.reroll()

	print(list1)

	again = str(input('Would you like to roll your dice again? Y/N  \n'))
	again = again.lower()
	while again != 'y' and again != 'n':
		print('That is not an option!')
		again = str(input('Would you like to roll your dice again? Y/N  \n'))
	if again == 'y':
		reroll1.reroll()
	print('Here are you final dice rolls: \n')
	print(list1)

elif again =='n':
	print('Here are you final dice rolls: \n')
	print(list1)

#Picking a cateogory Function

#Score Function
reroll1.chancethreefour()
print('\nScore:' + str(reroll1.total))
#Total Sum Function