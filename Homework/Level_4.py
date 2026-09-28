#Start lists for all the categories we will be sorting to
small = []
moderate = []
large = []
#Ask for expense numbers until user enters 0
#Add expenses to their designated list after 0 is entered and prepare to print them out
expense = float(input('Enter an expense or 0 to finish: '))
while expense != 0:
    if expense < 25:
        small.append(expense)
    elif expense <= 100:
        moderate.append(expense)
    else:
        large.append(expense)
    expense = float(input('Enter an expense or 0 to finish: '))

#Combine all expenses so we can calculate statistics
all_expenses = small + moderate + large

#Print out results
if len(all_expenses) == 0:
    print('No expenses were entered')
else:
    total = sum(all_expenses)
    count = len(all_expenses)
    average = total/count

    print('\n--- Expense Summary ---')
    print(f'Total number of expenses: {count}')
    print(f'Total expenses: ${total:,.2f}')
    print(f'Average expense: ${average:,.2f}')
    print(f'Smallest expense: ${min(all_expenses):,.2f}')
    print(f'Largest expense: ${max(all_expenses):,.2f}')
    print(f'Number of small expenses: {len(small)}')
    print(f'Number of moderate expenses: {len(moderate)}')
    print(f'Number of large expenses: {len(large)}')