import random

#List of available choices and dictionary mapping the choices to the ones they beat
choices = ['rock', 'paper', 'scissors']
winnings = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

#Asks how many rounds the player wants, only accepting odd numbers to leave a true winner
def get_rounds():
    rounds = input('How many rounds would you like to play: ')
    while True:
        if rounds.isdigit() and int(rounds) > 0 and int(rounds) % 2 == 1:
            return int(rounds)
        rounds = input('Sorry, the number must be an odd number. Please try again: ')

#Asks the player what their choice will be of the 3 available options, only accepting valid options
def get_player_choice():
    player_choice = input('Enter rock, paper, scissors: ').lower()
    while player_choice not in choices:
        print(f'Sorry, “{player_choice}” is not a valid choice. Please try again.')
        player_choice = input('Enter rock, paper, scissors: ').lower()
    return player_choice

#Runs the other programs in order, checks if the computer or the player won a certain round
def main():
    print('Welcome to Rock Paper Scissors!')
    rounds = get_rounds()
    player_w = 0
    comp_w = 0
    rounds_played = 0
    while rounds_played < rounds:
        player = get_player_choice()
        computer = random.choice(choices)
        print(f'The computer chose {computer}.')

#The variable player is used as key in a dictionary that returns a value.
#If that value is the same as the one the computer randomly picked, that means the player won that round
        if player == computer:
            print("Tie! Play again.")
        elif winnings[player] == computer:
            print('You won!')
            player_w += 1
            rounds_played += 1
        else:
            print('You lost!')
            comp_w += 1
            rounds_played += 1

    print("-------------------------------------------")
    print(f"Score — You: {player_w} | Computer: {comp_w}")
    if player_w > comp_w:
        print('You win!!!')
    else:
        print('You lost!!!')
    print('Thanks for playing!')

main()