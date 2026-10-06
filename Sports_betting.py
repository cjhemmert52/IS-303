import random

guess = 0
print('Welcome to the Higher/Lower Game')

def one_play(s):
    num_guesses = 0
    guess = int(input('Guess a number between 1 and 100: '))
    while not (guess >= 1 and guess <= 100):
        guess = int(input('Invalid number. Please try again: '))
    num_guesses += 1

    #Determine the nees of guess adjustment
    if guess > solution:
            print('Lower')
    elif guess < solution:
            print('Higher')
    elif guess == solution:
            print('You got it!')

#loop

    print(f'It took you {num_guesses} guesses.')

#Get a random number for the user to guess
solution = random.randint(1, 100)

while guess != solution:
      one_play(solution)
#Get and validate user input