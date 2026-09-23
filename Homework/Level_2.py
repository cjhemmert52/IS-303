#Basic formatting here
print('================================')
print('ROAD TRIP PLANNER')
print('================================')

#This is where we will gather our information
traveler_name = input('What is your name? ')
destination = input('Where are you traveling? ')
distance = int(input('How many miles is the trip one way? '))
car_mpg = int(input('What is your vehicle\'s miles per gallon? '))
gas_price = float(input('What is the price per gallon? '))
num_travelers = int(input('How many travelers are going? '))

#Calculate data
total_dist = distance * 2
total_gas = total_dist/car_mpg
total_cost = total_gas * gas_price
cost_per_person = total_cost/num_travelers

#Print out the list of results
print('================================')
print('TRIP SUMMARY')
print('================================')
print(f'Traveler: {traveler_name.upper()}')
print(f'Destination: {destination}')
print(f'Gallons of Gas: {total_gas}')
print(f'Gas cost: ${total_cost}')
print(f'Cost per traveler: ${cost_per_person}')
print('================================')
print('Have a great trip!')