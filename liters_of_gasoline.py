values = input().split()
time = float(values[0])
speed = float(values[1])
distance_traveled = time * speed
liters_of_gasoline = distance_traveled / 12
print(f'{liters_of_gasoline:.3f}')