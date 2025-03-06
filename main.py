class Car:
    def __init__(self, brand, model, speed, fuel):
        self.brand = brand
        self.model = model
        self._speed = speed
        self._fuel = fuel

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_speed(self):
        return self._speed

    def get_fuel(self):
        return self._fuel


    def set_speed(self, speed):
        if self._speed <= 200:
            self._speed = 200

    def set_fuel(self, fuel):
        if self._fuel > 0:
            self._fuel = 0


car_1 = Car("Resonator", 300, 15, 20)
car_2 = Car("Linguini", 250, 15, 25)

print(car_1.get_brand())
print(car_2.model)

car_1.get_speed()
car_2.get_speed()

print(car_1.get_speed())
print(car_2.get_speed())

car_1.set_fuel(15)
car_2.set_fuel(1)

print(car_1.get_fuel())
print(car_2.get_fuel())