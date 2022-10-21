contacts = {
    'carol@gmail.com': {'name': 'Carolina', 'phone': '19 2345-6789'},
}

copy_contacts = contacts.copy()
copy_contacts['carol@gmail.com'] = {'name': 'Carol'}

print(contacts['carol@gmail.com']) # {'name': 'Carolina', 'phone': '19 2345-6789'}
print(copy_contacts['carol@gmail.com']) # {'name': 'Carol'}