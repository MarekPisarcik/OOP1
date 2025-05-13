

# Zakladna trieda Shape
class Shape:
    def __init__(self,a):
        self.a = a

    def area_square(self):
        a = int(input("Zadaj cislo"))
        return a * a

stvorec = Shape("0")
#stvorec.area_square()