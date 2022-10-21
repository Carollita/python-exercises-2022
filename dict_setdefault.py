contact = {'name': 'Carolina', 'phone': '19 2345-6789'}

# exist value
contact.setdefault('name', 'Carolina')
print(contact)
# {'name': 'Carolina', 'phone': '19 2345-6789'}

# do not exist value
contact.setdefault('age', 18)
print(contact)
# {'name': 'Carolina', 'phone': '19 2345-6789', 'age': 18}