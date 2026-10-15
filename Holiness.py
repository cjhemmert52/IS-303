from SecondFile import is_odd

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if is_odd(num):
        print(f'{num} is odd.')
    else:
        print(f'{num} is even.')