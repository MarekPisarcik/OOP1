from OOP2 import Vehicle


class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        super().__init__(brand, speed)

        self.num_doors = num_doors

       def describe(self):
           return f"Znacka: {self.brand}, Maximalna rychlost: {self.speed}, Pocet dvery {self.num_doors}"