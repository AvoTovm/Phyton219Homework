from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        return f"{super().display_info()} with {self.doors} doors"

class Plane(Vehicle):
    def __init__(self, make, model, year, wingspan):
        super().__init__(make, model, year)
        self.wingspan = wingspan

    def display_info(self):
        return f"{super().display_info()} with a wingspan of {self.wingspan} meters"

class Boat(Vehicle):
    def __init__(self, make, model, year, length):
        super().__init__(make, model, year)
        self.length = length

    def display_info(self):
        return f"{super().display_info()} with a length of {self.length} meters"

class RaceCar(Car):
    def __init__(self, make, model, year, doors, top_speed):
        super().__init__(make, model, year, doors)
        self.top_speed = top_speed

    def display_info(self):
        return f"{super().display_info()} capable of {self.top_speed} km/h"


race_car = RaceCar("BMW", "M8 GTE", 2018, 2, 300)
print(race_car.display_info())

boat = Boat("Yamaha", "WaveRunner", 2021, 10)
print(boat.display_info())

plane = Plane("Boeing", "747", 2019, 68)
print(plane.display_info())
