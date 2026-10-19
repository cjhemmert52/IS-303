from Level_67_functions import choose_word, choices, get_guess, evaluate_guess, display_guess, has_won

#Welcom message gets printed and secret word is chosen.
def main():
    print('Welcome to Mystery Wordle!')
    print('\nGuess the five-letter word.')
    print('\nG = correct letter and position')
    print('Y = correct letter, wrong position')
    print('- = letter is not found in the word')
    secret = choose_word(choices)
    max_attempts = 6
    
    #The funcions in the other file get called until max_attempts is reached.
    for attempt in range(1, max_attempts + 1):
        print(f'\nAttempt {attempt} of {max_attempts}')
        guess = get_guess()
        result = evaluate_guess(secret, guess)
        display_guess(guess, result)
        
        #If at any point during the loop the has_won function returns 'True', the loop ends
        #and the win message gets printed.
        if has_won(secret, guess):
            print(f'You won in {attempt} guesses!')
            return
    print(f'\nOut of guesses. The word was {secret.upper()}')
        
main()