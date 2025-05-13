from Task1_main import Shape


class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a)
        
        self.b = b

    def area_rectangle(self):
        a = int(input("Zadaj cislo"))
        b = int(input("Zadaj cislo"))
        return a * b

obdlznik = Rectangle(0, 0)
#obdlznik.area_rectangle()