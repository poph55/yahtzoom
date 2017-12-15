import random
from DiceClass import Dice
#Class for our game Yahtzoom
class Yahtzoom:
    def __init__(self, list1):
        self.list1 = list1

    #Function that selects which one that you want to rhttp://collabedit.com/eroll
    def reroll(self):
        rollagain = []
        rerollinput = input("Which dice would you like to reroll?")
        while 1==1:
            rerollinput = input('Which dice would you like to reroll?')
            rollagain.append(rerollinput)
        die6 = Dice()
        clock = rollagain.len()
        while clock > 0:
            clock -= 1
            self.list1[rollagain[clock-1]-1] = die6.roll()	
        
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
