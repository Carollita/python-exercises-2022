contacts = {
    'carol@gmail.com': {'name': 'Carol', 'phone': '19 2345-6789'},
    'elis@gmail.com': {'name': 'Elis', 'phone': '19 1234-5678'},
    'gabriel@gmail.com': {'name': 'Gabriel', 'phone': '19 1234-8765'},
}

print('carol@gmail.com' in contacts) # True
print( 'leticia@gmail.com' in contacts) # False
print('age' in contacts['carol@gmail.com']) # False
print('phone' in contacts['carol@gmail.com']) # True