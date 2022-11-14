class Animal:
    def __init__(self, num_legs):
        self.num_legs = num_legs

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

class Mammal(Animal):
    def __init__(self, fur, **kw):
        self.fur = fur
        # super().__init__(num_legs = kw['num_legs'])
        super().__init__(**kw)

class Bird(Animal):
    def __init__(self, beak, **kw):
        self.beak = beak
        super().__init__(**kw)

class NoisesMixin:
    def noises(self):
        return 'Miau'

class Cat(Mammal, NoisesMixin):
    pass

class Lion(Mammal):
    pass


class Platypus(Mammal, Bird):
    def __init__(self, beak, fur, num_legs):
        super().__init__(fur=fur, beak=beak, num_legs=num_legs)
        # print(Platypus.__mro__)
        # print(Platypus.mro())
        # (<class '__main__.Platypus'>, <class '__main__.Mammal'>, <class '__main__.Bird'>, <class '__main__.Animal'>, <class 'object'>)

my_cat = Cat(num_legs=4, fur='black')
print(my_cat)
# Cat: fur=black, num_legs=4

my_platypus = Platypus(num_legs=4, fur='brown', beak='black')
print(my_platypus)
# Platypus: fur=brown, num_legs=4

print(my_cat.noises())