blah = [1, 7, 19, 22, 24, 8]
evens = []
odds = []

for num in blah:
    if num % 2 == 0:
        evens.append(num)
        print(f'{num} is even')
    elif num % 2 != 0:
        odds.append(num)
        print(f'{num} is odd')

print(f'There are {len(evens)} even numbers.')
print(f'There are {len(odds)} odd nunbers.')
    
