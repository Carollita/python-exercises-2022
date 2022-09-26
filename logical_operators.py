balance,  withdraw, credit_limit, special_account = 1490, 700, 400, True

# and operator
print(balance >= withdraw and balance <= credit_limit)
# False

# or operator
print(balance >= withdraw or balance <= credit_limit)
# True

# not operator
contacts = []

print(not 2 > 4)
# True

print(not contacts)
# True

print(not 'Hello, world')
# False

print(not '')
# True

check_account_balance = balance >= withdraw and balance <= credit_limit
check_special_account_balance = special_account and balance >= withdraw
print(check_account_balance or check_special_account_balance)
# print((balance >= withdraw and balance <= credit_limit) or (special_account and balance >= withdraw))