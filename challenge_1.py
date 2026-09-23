#- Ask how many numbers the user wants to enter
#- Use a loop to collect the numbers





numbers = [5, 16, -3, 0, 12]
#If a number is < 0, add it to a count of negatives
#If a number is > 0, add it to a count of positives
#If a number is 0, add it to its own count
positives_count = 0
negatives_count = 0
zeroes_count = 0
for number in numbers:
    if number < 0:
        print('Negative')
        negatives_count += 1
    elif number > 0:
        print('Positive')
        positives_count += 1
    elif number == 0:
        print('Zero')
        zeroes_count += 1

print(f'Count of positives: {positives_count}')
print(f'Count of negatives: {negatives_count}')
print(f'Count of zeroes: {zeroes_count}')
