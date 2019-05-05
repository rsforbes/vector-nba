import re
import sys

def select_game(count):
    while True:
        value = input(f'\nSelect a game (1-{count}) or (q)uit: ')
        test_quit(value)  
        if re.match(f"^[1-{count}]$", value):
            return int(value)


def select_team():
    while True:
        value = input('\nSelect a team (v,h) or (q)uit: ')
        test_quit(value)              
        if re.match("^[v|h]$", value): 
            return value

def test_quit(input):
    if input == 'q': exit()
    
