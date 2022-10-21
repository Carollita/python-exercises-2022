print(dict.fromkeys(['name', 'phone']))
# {'name': None, 'phone': None}

print(dict.fromkeys(['name', 'phone'], 'empty'))
# {'name': 'empty', 'phone': 'empty'}

person = {'name': 'Carolina', 'age': 18}
print(person.fromkeys(['adress', 'city']))
# {'adress': None, 'city': None}   