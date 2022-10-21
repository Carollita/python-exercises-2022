# Update
contact = {
    'carol@gmail.com': {'name': 'Carolina', 'phone': '19 2345-6789'},
}

# exist value
contact.update({'carol@gmail.com' : {'name': 'Carol'}})
print(contact)
# {'carol@gmail.com': {'name': 'Carol'}}

# do not exist value
contact.update({'jennifer@gmail.com' : {'name': 'Jennifer', 'phone': '19 2335-6666'}})
print(contact)
# {'carol@gmail.com': {'name': 'Carol'}, 'jennifer@gmail.com': {'name': 'Jennifer', 'phone': '19 2335-6666'}}

# Pop
contact = {
    'carol@gmail.com': {'name': 'Carolina', 'phone': '19 2345-6789'},
}

print(contact.pop('carol@gmail.com')) # remove {'name': 'Carolina', 'phone': '19 2345-6789'}
print(contact) # {}
print(contact.pop('carol@gmail.com', 'We do not find this contact.')) # We do not find this contact.

contact = {
    'carol@gmail.com': {'name': 'Carolina', 'phone': '19 2345-6789'},
}

contact.popitem() # remove {'name': 'Carolina', 'phone': '19 2345-6789'}]
print(contact) # {}
contact.popitem() # KeyError