#Runner Class
from DiceClass import Dice
#from YahtzeeClass import Yahtzoom

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

#Picking a cateogory Function

#Score Function

#Total Sum Function