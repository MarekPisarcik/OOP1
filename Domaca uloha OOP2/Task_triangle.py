from Task1_rectangle import Rectangle


class Triangle(Rectangle):
    def __init__(self, a, b,):
        super().__init__(a, b)

    def area_triangle(self):
        result = self.area_rectangle() / 2
        return print(result)

trojuholnik = Triangle(0, 0)
#trojuholnik.area_triangle()