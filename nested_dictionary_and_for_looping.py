contacts = {
    'carol@gmail.com': {'name': 'Carol', 'phone': '19 2345-6789'},
    'elis@gmail.com': {'name': 'Elis', 'phone': '19 1234-5678'},
    'gabriel@gmail.com': {'name': 'Gabriel', 'phone': '19 1234-8765'},
}

print(contacts['carol@gmail.com']['phone'])
# 19 2345-6789

for key in contacts:
    print(key, contacts[key])
# carol@gmail.com {'name': 'Carol', 'phone': '19 2345-6789'}    
# elis@gmail.com {'name': 'Elis', 'phone': '19 1234-5678'}      
# gabriel@gmail.com {'name': 'Gabriel', 'phone': '19 1234-8765'}

for key, value in contacts.items():
    print(key, value)
# carol@gmail.com {'name': 'Carol', 'phone': '19 2345-6789'}    
# elis@gmail.com {'name': 'Elis', 'phone': '19 1234-5678'}      
# gabriel@gmail.com {'name': 'Gabriel', 'phone': '19 1234-8765'}

contacts.clear()
print(contacts) # {}