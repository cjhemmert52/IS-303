import random
choices = ['plane', 'crane', 'train', 'earth', 'chair', 'slate', 'shoes', 'socks', 'board']

def choose_word(choices):
    secret = random.choice(choices)
    return secret

def get_guess():
    guess = str(input('Enter a five-letter word: ')).lower().strip()
    while len(guess) != 5:
        guess = str(input('Invalid guess, please try again ')).lower().strip()
    return guess

def evaluate_guess(secret, guess):
    result = ''
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += 'G'
        elif guess[i] in secret:
            result += 'Y'
        else:
            result += '-'
    return result

def display_guess(guess, result):
    print(f'Guess: {' '.join(guess.upper())}')
    print(f'Feedback: {' '.join(result)}')

def has_won(secret, guess):
    return guess == secret