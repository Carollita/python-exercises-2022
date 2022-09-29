while True:
    number = int(input('Number: '))

    if number == 10:
        break

    print(number)

for number in range(100):
    if number == 10:
        break

    print(number, end=' ')

print()

for number in range(100):
    if number == 10:
        continue

    print(number, end=' ')