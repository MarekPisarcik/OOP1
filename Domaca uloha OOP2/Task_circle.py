from Task1_main import Shape


class Circle(Shape):
    def __init__(self,a):
        super().__init__(a)

    def area_circle(self):

        result = self.area_square() * 3.14
        print(result)

kruh = Circle(0)
#kruh.area_circle()