import math


class Line(object):
    DEFAULT_COLOR = 0

    def __init__(self, point1, point2, color=DEFAULT_COLOR):
        self.start_point = point1
        self.stop_point = point2
        self.color = color

    def get_start(self):
        return self.start_point

    def get_stop(self):
        return self.stop_point

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color
        return self.color

    def get_xs(self):
        x_s = [self.start_point.get_x(), self.stop_point.get_x()]
        return x_s

    def get_ys(self):
        y_s = [self.start_point.get_y(), self.stop_point.get_y()]
        return y_s

    def xy_dist(self):
        """Returns x and y dist as separate entities in list"""
        x = self.get_stop().get_x()-self.get_start().get_x()
        y = self.get_stop().get_y()-self.get_start().get_y()
        return [x, y]

    def dist(self):
        """Returns line distance"""
        xy = self.xy_dist()
        dist = math.sqrt(xy[0]**2+xy[1]**2)
        return dist


class Point(object):
    def __init__(self, x, y, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def points(self):
        return [self.x, self.y, self.z]

    def point_str(self):
        return "%d, %d, %d" % (self.get_x(), self.get_y(), self.get_z())
