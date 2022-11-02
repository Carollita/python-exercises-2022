def welcome01():
    print('Welcome!')

def welcome02(name):
    print(f'Welcome, {name}!')

def welcome03(name = 'Camila'):
    print(f'Welcome, {name}!')

welcome01()
welcome02(name = 'Lara')
welcome03()
welcome03(name = 'Barbara')

def sum(x,y):
    return x + y

def show_result(x, y, function):
    result = function(x, y)
    print(f'Result: {x} + {y} = {result}')

show_result(10, 8, sum)