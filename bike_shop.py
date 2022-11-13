class Bike:
    def __init__(self, color, brand, year, price):
        self.color = color
        self.brand = brand
        self.year = year
        self.price = price
        self.gear = 1

    def honk(self):
        print('PLIM PLIM \U0001f4e2')

    def stop(self):
        print('STOP \U0001f6a6')

    def run(self):
        print('RUN \U0001f6b5\U0001f3fe')
    
    def get_color(self):
        return self.color

    def __str__(self):
        # return f'Bike: {self.color}, {self.brand}, {self.year}, {self.price}'
        return f"{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"

    def change_gear(self, gear_num):
        print('Changing bike gear')
        _self = self

        def _change_gear():
            if gear_num != _self.gear:
                print('Bike gear changed \u2714\uFE0F')
            else:
                print('You didn\'t change the gear of the bike 	\u274C')
        
        _change_gear()

bike_id_1 = Bike('blue', 'shimano', '2022', '993,52') 

print(bike_id_1.color, bike_id_1.brand, bike_id_1.year, bike_id_1.price)
# blue shimano 2022 993,52

bike_id_1.honk()
# PLIM PLIM 📢

bike_id_1.stop()
# STOP 🚦

bike_id_1.run()
# RUN 🚵🏾

bike_id_2 = Bike('black', 'monark', '2020', '740,80') 
print(bike_id_2.color, bike_id_2.brand, bike_id_2.year, bike_id_2.price)
# black monark 2020 740,80

Bike.honk(bike_id_2)
# PLIM PLIM 📢

print(bike_id_2.get_color())
# black

print(bike_id_2)
# Bike: color=black, brand=monark, year=2020, price=740,80, gear=1

Bike.change_gear(bike_id_2, 24)
# Changing bike gear
# Bike gear changed ✔️

Bike.change_gear(bike_id_2, 1)
# Changing bike gear
# You didn't change the gear of the bike  ❌