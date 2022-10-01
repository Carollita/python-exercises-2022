name = 'Melissa'
age = 28
fruit = 'strawberry'
profile = {'name': 'Melissa', 'age': 28, 'fruit':'strawberry'}

print('My name is %s, I am %d years old and my favorite fruit is %s.' %(name, age, fruit))

print('My name is {}, I am {} years old and my favorite fruit is {}.'.format(name, age, fruit))
print('My name is {2}, I am {0} years old and my favorite fruit is {1}.'.format(age, fruit, name))
print('My name is {n}, I am {a} years old and my favorite fruit is {f}.'.format(n=name, a=age, f=fruit))
print('My name is {name}, I am {age} years old and my favorite fruit is {fruit}.'.format(**profile))

print(f'My name is {name}, I am {age} years old and my favorite fruit is {fruit}.')

PI = 3.14159
print(f'Valor de PI: {PI:.2f}')
# Valor de PI: 3.14

print(f'Valor de PI: {PI:10.2f}')
# Valor de PI:       3.14