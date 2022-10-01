list = []

list.append(1)
list.append('Hi')
list.append([2, 3, 4])

print(list) # [1, 'Hi', [2, 3, 4]]

another_list = list.copy()
print(list) # [1, 'Hi', [2, 3, 4]]

print(id(list), id(another_list))

another_list[0] = 9
print(list, another_list) # [1, 'Hi', [2, 3, 4]] [9, 'Hi', [2, 3, 4]]

list.clear()
print(list) # []