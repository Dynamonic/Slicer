from SliceTest.point import Point


class Edge(object):

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_points(self):
        return [self.point1, self.point2]

    def line_length(self):
        x = self.point2.x-self.point1.x
        y = self.point2.y-self.point1.y
        lin_length = (x ** 2 + y ** 2) ** (1/2)
        return lin_length

    def slope(self):
        x = self.point2.x - self.point1.x
        y = self.point2.y - self.point1.y
        if x != 0:  # Make sure to not divide by zero!
            slope = y / x
        else:
            slope = None
        return slope

    def y_intercept(self):
        slope = self.slope()
        if slope is not None:
            b = slope * self.point1.x - self.point1.y
            return b
        else:
            return None

    def x_intercept(self):
        inv_slope = self.inv_slope()
        if inv_slope is not None:
            b = inv_slope * self.point1.y - self.point1.x
            return b
        else:
            return None

    def inv_slope(self):
        x = self.point2.x - self.point1.x
        y = self.point2.y - self.point1.y
        if y != 0:  # Make sure to not divide by zero!
            slope = x / y
        else:
            slope = None
        return slope

    def point_on_line(self, point):
        x = self.point1.x - self.point2.x
        y = self.point1.y - self.point2.y
        if x != 0:  # Make sure to not divide by zero!
            slope = y / x
            intercept = self.point1.y - (slope*self.point1.x)

            if min(self.point1.x,self.point2.x) <= point.x <= max(self.point1.x,self.point2.x):
                if point.y == slope*point.x + intercept:
                    return True
            return False
        elif y != 0:  # invert axis to not divide by zero
            slope = x/y
            intercept = self.point1.x - (slope*self.point1.y)
            if min(self.point1.y, self.point2.y) <= point.y <= max(self.point1.y, self.point2.y):
                if point.x == slope*point.y + intercept:
                    return True
            return False
        else:  # edge case where line is just a point
            if self.point1.x == point.x and self.point1.y == point.y:
                return True
            else:
                return False

