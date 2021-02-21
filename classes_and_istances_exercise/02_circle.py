class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_circumference(self):
        return self.pi * (self.radius * 2)