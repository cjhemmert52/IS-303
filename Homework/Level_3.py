import random

#Random number generator
def get_number():
    return random.randint(1,100)

#Function that prints the results based on number of attempts
def get_feedback(attempts):
    if attempts <= 3:
        return "Amazing!"
    elif attempts <= 5:
        return "Impressive!"
    elif attempts <= 7:
        return "Good job!"
    elif attempts <= 9:
        return "Took a little longer, but you got there!"
    else:
        return "You need to lock in."

#Function that tracks the amount of attempts and outputs 'Higher' or 'Lower'
#Based on how far from the random number the guess is
def guessing_game():
    number = get_number()
    attempts = 0
    print('I\'m thinking of a number 1 to 100')
    while True:
        guess = int(input('Enter your guess: '))
        attempts += 1
        if guess > number:
            print('Lower!')
        elif guess < number:
            print('Higher!')
        else:
            print('Correct!')
            print(f'You got it in {attempts} guesses')
            print(get_feedback(attempts))
            break

def main():
    while True:
        guessing_game()
        play_again = input('Play again? (Y/N): ')
        if play_again.lower() != 'y':
            print('Thanks for playing!')
            break

main()