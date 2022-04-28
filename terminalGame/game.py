import time
import random
from os import system, name

from misc.functions import *
from misc.messages import *
from classes.player import *
from classes.numGame import *

playerInput = str(input(welcome))
player = Player(playerInput)
playing = True

while playing:
    message = input(f'\nWelcome, {player.name}!\nWould you like to play a game?\ny/n\n')
    message = message.split()
    if message[0] == 'n':
        message = print(noGame)
        playing = False
    else:
        message = print(yesGame)
        gameList = input("\n\nPlease chose a game from the list by selecting it's coresponding number:\n________________________________________________________________________\n________________________________________________________________________\n\n\n1. Guess the number\n\n")
        gameList = gameList.split()
        if gameList[0] == '1':
            message = print(enterNumGame)
            clear()
            numGame = GuessTheNumber()
            numGame.start()
        else:
            message = print(badInput)
            playing = False