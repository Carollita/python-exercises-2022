name = str(input('What is your name? '))
age = int(input('How old are you? '))

if age >= 18:
    print(f'{name} is over 18!')
else:
    print(f'{name} is underage.')