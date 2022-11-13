class Dog:
    def __init__(self, name, color, awake=True):
        print(f'------------- initializing -------------')
        self.name = name
        self.color = color
        self.awake = awake

    def __del__(self):
        print(f'------------- Removing {self.name} -------------')

    def bark(self):
        print('Au au \U0001f436')

def adopt_dog():
    adopted_dog = Dog('Pretinho', 'Black', False)
    print(adopted_dog.name)

my_dog = Dog('Pipoca', 'Yellow')
my_dog.bark()
# Au au 🐶
adopt_dog()

print('Au au au au')
print('Au au au au')
del my_dog
print('...')