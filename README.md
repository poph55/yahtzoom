# yahtzoom
is yahtzee.!


Class Yahtzoom:
	
	functions:

		Roll
			-define a single die as a random number, 1-6
			-run this function 5 times for each of the starting dice

		Re-Roll
			-allow the user to select which of the dice the user wants to re-roll, and which to keep
			-append the ones to be re-rolled to a list
			-use the Roll function to to re-roll the dice in the list

		ScoreSelect
			-allow the user to select which score block they are filling out with their roll
			-the following functions will run if the user chooses that particular score block

		Ones
			-adds up all of the 1's rolled and stores that number as the variable "Ones"
		Twos
			-adds up all of the 2's rolled and stores that number as the variable "Twos"
		Threes
			-adds up all of the 3's rolled and stores that number as the variable "Threes"
		Fours
			-adds up all of the 4's rolled and stores that number as the variable "Fours"
		Fives
			-adds up all of the 5's rolled and stores that number as the variable "Fives"
		Sixes
			-adds up all of the 6's rolled and stores that number as the variable "Sixes"
		Chance
			-adds up all of the dice on the board, if this value is 17, "Chance" is stored as 35, otherwise, store "Chance" as the sum of all dice on the board
		FullHouse
			-Checks to see if there exists exactly 2 of one number, and exactly three of another number. If true, the variable "FullHouse" stores 25, if not, it stores 0
		SmallStraight
			-Checks to see if there is a string of either "1,2,3,4", "2,3,4,5", or "3,4,5,6" and if any of these occur, the variable "SmallStraight" stores 30, if not, it stores 0
		LargeStraight
			-Checks to see if there is a string of "1,2,3,4,5" or "2,3,4,5,6" and if either of these occur, the variable "LargeStraight" stores 40, if not it stores 0
		ThreeofKind
			-Checks to see if there are three of any number, if there is, sum all the dice on the board and store as the variable "ThreeofKind"
		FourofKind
			-Checks to see if there are four of any number, if there is, sum all the dice on the board and store as the variable "FourofKind"
		Yahtzoom
			-Checks to see if there are 5 of any number, if there is, the variable "Yahtzoom" stores 50, if not it stores 0

