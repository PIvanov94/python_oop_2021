from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance(self, x, y):
        return sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
