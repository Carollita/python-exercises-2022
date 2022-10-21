contacts = {
    'carol@gmail.com': {'name': 'Carolina', 'phone': '19 2345-6789'},
}

# print(contacts['adress']) return KeyError

print(contacts.get('adress')) # None
print(contacts.get('adress', {})) # {}
print(contacts.get('carol@gmail.com', {})) # {'name': 'Carolina', 'phone': '19 2345-6789'}

print(contacts.items())
# dict_items([('carol@gmail.com', {'name': 'Carolina', 'phone': '19 2345-6789'})])

print(contacts.keys())
# dict_keys(['carol@gmail.com'])

print(contacts.values())
# dict_values([{'name': 'Carolina', 'phone': '19 2345-6789'}])