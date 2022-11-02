def calculator(num):
    return sum(num)

def predecessor_and_successor(num):
    predecessor = num -1
    successor = num + 1
    return predecessor, successor

def cost():
    print('cost: R$ 12,00')

print(calculator([2, 4, 6])) # 12
print(predecessor_and_successor(8)) # (7, 9)
print(cost()) # return None