person = {'name': 'Carolina', 'age': 18}
# or 
another_person = dict(name = 'Carolina', age = 18)

person['phone'] = '19 2345-6789'

print(person)
# {'name': 'Carolina', 'age': 18, 'phone': '19 2345-6789'}

customer = {'name': 'Rebecca', 'age': 22, 'phone': '19 9876-5432'}
customer['name'] # Rebecca
customer['age'] # 22
customer['phone'] # 19 9876-5432

customer['name'] = 'Bea'
customer['age']  = 17
customer['phone'] = '19 7698-3254'

print(customer)
# {'name': 'Bea', 'age': 17, 'phone': '19 7698-3254'}