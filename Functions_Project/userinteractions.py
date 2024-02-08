# Create a simple program to solidify concepts on the guide.py file
# Lets create a program that will display a list of items and lets a user choose an index position and an input value 
# Replace the value at index position with user's chosen input value 

from curses.ascii import isdigit
from random import choice
import re


game_list = [0,1,2]

def display_game(game_list):
    print('Here is the current list: ')
    print(game_list)

display_game_result = display_game(game_list)
print(display_game_result)

def position_choice():
    choice = 'Wrong'
    while choice not in ['0','1','2']:
        choice = input('Pick a position (0,1,2): ')
        if choice not in ['0','1','2']:
            print('Sorry, invalid choice! ')
    
    return int(choice)

def replacement_choice(game_list, position):
    user_placement = input('Type a string to place at position: ')
    game_list[position] = user_placement
    return game_list
test_replacement_choice = replacement_choice(game_list,1)
print(test_replacement_choice)

def gameon_choice():
    choice = 'Wrong'
    while choice not in ['Y','N']:
        choice = input('Keep playing? (Y or N)')
        if choice not in ['Y','N']:
            print('Sorry, I don\'t understand, please choose Y or N ') 
    if choice == 'Y':
        return False
    else:
        return False
    
gameon = True
game_list = [0,1,2]

while gameon:
    display_game(game_list)
    
    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    gameon = gameon_choice()