import random
from os import system, name
from .player import *

class GuessTheNumber:
    def __init__(self):
        self.answer = 0
        self.leave = 0

    def getRandomNumber(self):
        self.answer = random.randint(1,10)
        self.answer
        return self.answer
    
    def checkInput(self, choice):
        if choice > 10 or choice < 1:
            message = print("That number is out of the range of possible answers.\n")
            self.leave = 0
            return self.leave
        else:
            if choice == self.answer:
                message = print("You guessed correct!!\n")
                message = print("Thank you for playing\nExiting to main screen\n\n")
                self.leave = 1
                return self.leave
            if choice > self.answer:
                message = print(f"Your guess of {choice} was too high try again")
                self.leave = 0
                return self.leave
            if choice < self.answer:
                message = print(f"Your guess of {choice} was too low try again")
                self.leave = 0
                return self.leave
            else:
                message = print("Sorry that was incorrect\n\n")
                self.leave = 0
                return self.leave

    def start(self):
        playerInput = str(input('Please remind me of your name\n\n'))
        player = Player(playerInput)
        self.getRandomNumber()
        # self.print()
        game = True
        while game:
            levelChoice = input("Please chose the level you wish to play form the list by typing the coresponding number:\n\n1. Advanced speed round\n2. Basic\n\n")
            levelChoice = levelChoice.split()
            if levelChoice == '2':
                choice = input(f"\n\n{player}, please chose a number between 1-10\n  ")
                choice = choice.split()
                message = print(f"\nYou have chosen: {choice[0]}\n")
                self.checkInput(int(choice[0]))
                if self.leave == 1:
                    game = False
            else:
                message = print(f"\n{player.name} you have 3 tries to guess the right number\n")
                round = [1,2,3]
                for r in round:
                    # print(r)
                    if self.leave == 1:
                        game = False
                    elif r <= 2:
                        message = print(f"ROUND {r}")
                        choice = input(f"\n\n{player.name}, please chose a number between 1-10\n  ")
                        choice = choice.split()
                        self.checkInput(int(choice[0]))
                        # if self.leave == 1:
                        #     game = False
                    else:
                        message = print(f"ROUND {r}, Last Round")
                        choice = input(f"\n\n{player.name}, please chose a number between 1-10\n  ")
                        choice = choice.split()
                        self.checkInput(int(choice[0]))
                        message = print(f"Sorry you are out of turns")
                        if self.leave == 1:
                            game = False
                self.leave = 1
                game = False