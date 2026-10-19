import random
choices = ['plane', 'crane', 'train', 'earth', 'chair', 'slate', 'shoes', 'socks', 'board']

#Generates a random word of the available choices
def choose_word(choices):
    secret = random.choice(choices)
    return secret

#Gathers the players 5 letter word as a guess. If it's shorter or longer than 5 letters
#or contains a number, the input is invalid and asks for a new guess.
def get_guess():
    guess = str(input('Enter a five-letter word: ')).lower().strip()
    while len(guess) != 5 or not guess.isalnum():
        guess = str(input('Invalid guess, please try again ')).lower().strip()
    return guess

#Looks at each indivudual letter in both the guess and secret.
#'G' is what gets added to result if the position and letter are correct.
#'Y' is what gets added to result if the letter is in the word at all.
#Result gets sent to another function to be printed
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

#Prints the guess and the result from evaluate_guess with spaces between each letter
def display_guess(guess, result):
    print(f'Guess: {" ".join(guess.upper())}')
    print(f'Feedback: {" ".join(result)}')

#Returns 'True' if the players guess matches the secret word exactly
def has_won(secret, guess):
    return guess == secret