# Identity operators are used to compare the memory location of two objects

name = 'Carol'
client_name = name
balance,  withdraw = 390, 390

print(name is client_name)
# True

print(name is not client_name)
# False

print(balance is withdraw)
# True

print(withdraw is balance)
# True