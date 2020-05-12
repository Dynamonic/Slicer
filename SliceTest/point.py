
class Point(object):
    """Class for a 3D point. currently only used for 2D"""
    def __init__(self, x, y, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    # def __init__(self, list_xyz):
    #     self.x = list_xyz[0]
    #     self.y = list_xyz[1]
    #     self.z = list_xyz[2]

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def point_str(self):
        return "%d, %d, %d" % (self.get_x(), self.get_y(), self.get_z())
