from SliceTest.point import Point


class TxtReader(object):

    DEFAULT_NAME = "out.txt"
    data = []

    def __init__(self, filename=DEFAULT_NAME):
        self.__run(filename)

    def getData(self):
        return self.data

    def __run(self, filename):
        f = open(filename, "r")
        contents = f.readlines()
        for line in contents:
            if line != "ON" and line != "OFF":
                xyz = line.split(",")
                point = Point(xyz[0], xyz[1], xyz[2])
                self.data.append(point)
            else:
                self.data.append(line)
        f.close()
