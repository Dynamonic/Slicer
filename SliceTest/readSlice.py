from SliceTest.point import Point


class SliceReader(object):
    """Reads in geometry slices and converts it into a list of points"""
    DEFAULT_NAME = "slice.txt"
    data = []

    def __init__(self, filename=DEFAULT_NAME):
        self.__run(filename)

    def getData(self):
        return self.data

    def __run(self, filename):
        """Opens and reads file contents line by line"""
        f = open(filename, "r")
        contents = f.readlines()
        for line in contents:
            xyz = line.split(",")
            point = Point(xyz[0], xyz[1], xyz[2])
            self.data.append(point)
        f.close()

