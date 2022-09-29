text = str(input('Write a text here: '))
vowels = 'AEIOU'

for letter in text:
    if letter.upper() in vowels:
        print(letter, end=' ')
else:
    print()