print('------------ Count to 03 ------------')
print(list(range(0, 4)))
# [0, 1, 2, 3]

print('------------ Count to 10 ------------')
for num in range(0, 11):
    print(num, end=' ')
# 0 1 2 3 4 5 6 7 8 9 10 

# 6 times table
print('\n------------ 6 times table ------------')
for number in range(0, 61, 6):
    # (start, stop, step)
    print(number, end=' ')