class Vehicle:
    def __init__(self, color, plate, wheels):
        self.color = color
        self.plate = plate
        self.wheels = wheels
    
    def start_engine(self):
        print('Starting the engine')

    def __str__(self):
        return self.color


class Motorcycle(Vehicle):
    pass

class Car(Vehicle):
    pass

class Truck(Vehicle):
    def __init__(self, color, plate, wheels, loaded):
        super().__init__(color, plate, wheels)
        self.loaded = loaded

    def is_loaded(self):
        print(f"{'Is' if self.loaded else 'Is not'} loaded.")

motorcycle_id_01 = Motorcycle('red', 'abc-1234', 2)
motorcycle_id_01.start_engine()
# Starting the engine

car_id_01 = Car('white', 'def-5678', 4)
car_id_01.start_engine()
# Starting the engine

truck_id_01 = Truck('green', 'ghi-9123', 8, True)
truck_id_01.start_engine()
# Starting the engine

truck_id_01.is_loaded()
# Is not loaded.
# car_id_01.is_loaded()
# AttributeError: 'Car' object has no attribute 'is_loaded'

print(truck_id_01)