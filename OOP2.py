


class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

     def describe(self):
        return f"Znacka: {self.brand}, Maximalna rychlost: {self.speed}"
