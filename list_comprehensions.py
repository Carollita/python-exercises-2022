numbers = [2, 4, 6, 7, 8, 9, 11]
even_numbers = []
exponentiation = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers) # [2, 4, 6, 8]

another_even_numbers = [num for num in numbers if num % 2 == 0]
print(another_even_numbers) # [2, 4, 6, 8]

for num in numbers:
        exponentiation.append(num ** 2)
print(exponentiation) # [4, 16, 36, 49, 64, 81, 121]

another_exponentiation = [num ** 2 for num in numbers]
print(another_exponentiation) # [4, 16, 36, 49, 64, 81, 121]