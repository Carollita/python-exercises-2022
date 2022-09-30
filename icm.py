values = input().split()

distance = int(values[0])
diameter1 = int(values[1])
diameter2 = int(values[2])

icm = distance / (diameter1 + diameter2)
print(f'{icm:.2f}')