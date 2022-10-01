cars = ['Ford', 'BMW', 'Volvo']

print(sorted(cars)) # ['BMW', 'Ford', 'Volvo']

print(sorted(cars, reverse=True)) # ['Volvo', 'Ford', 'BMW']

print(sorted(cars, key=lambda x: len(x))) # ['BMW', 'Ford', 'Volvo'] 
# Sort the list by the length of the values

print(sorted(cars, key=lambda x: len(x), reverse=True)) # ['Volvo', 'Ford', 'BMW'] 
# Sort the list by the length of the values and reversed