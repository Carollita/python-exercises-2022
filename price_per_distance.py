distance_traveled = float(input('Distance Traveled: '))
days = int(input('Travel Days: '))

cost = (60 * days) + (0.15 * distance_traveled)

print(f'The final cost for {days} days of travel and {distance_traveled} km traveled is {cost}')