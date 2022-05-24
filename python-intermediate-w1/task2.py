class Point2D:
    _points = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__class__._points += 1

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

    @classmethod
    def get_points(cls):
        return cls._points

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2 + (self.z - p.z) ** 2) ** 0.5


A = Point2D(3, 2)
B = Point2D(8, 14)
print("Distance between points A and B equals", A.distance(B))
C = Point3D(1, 2, 6)
D = Point3D(8, 7, 10)
print("Distance between points C and D equals", Point3D.distance(C, D))
print(f"There is {Point3D.get_points()} points")
