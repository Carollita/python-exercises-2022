contacts = {
    'carol@gmail.com': {'name': 'Carol', 'phone': '19 2345-6789'},
    'elis@gmail.com': {'name': 'Maria', 'phone': '19 1234-5678'},
}

del contacts['carol@gmail.com']['phone']
print(contacts)
# {'carol@gmail.com': {'name': 'Carol'}, 'elis@gmail.com': {'name': 'Maria', 'phone': '19 1234-5678'}}

del contacts['elis@gmail.com']
print(contacts)
# {'carol@gmail.com': {'name': 'Carol'}}

# del contacts
# print(contacts)
# NameError: name 'contacts' is not defined