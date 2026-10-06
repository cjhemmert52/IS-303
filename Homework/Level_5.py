import random

#List of available choices and dictionary mapping the choices to the ones they beat
choices = ['rock', 'paper', 'scissors']
winnings = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

def get_rounds():
    print('Welcom to rock, paper, scissors!')
    rounds = input('How many rounds would you like to play? ')
    while True:
        if int(rounds) > 0 and int(rounds) % 2 == 1:
            return rounds
        rounds = ('Invalid input, please try again')

def get_player_choice():
    computer_choice = random.choice(choices)
    player_choice = input('Enter rock, paper, or scissors: ')

