class Rectangle:
    def __init__(self):
        print("Inside init of Rectangle")

    def area(self, x, y):
        return x * y


class Squire(Rectangle):
    def __init__(self):
        print("Inside init of Square")


r = Rectangle()
sq = Squire()
area = sq.area(2,2)
print(area)
