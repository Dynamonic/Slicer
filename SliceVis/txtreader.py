from SliceVis.vis_geometry import Point


class TxtReader(object):

    DEFAULT_NAME = "out.txt"
    data = []

    def __init__(self, filename=DEFAULT_NAME):
        self.__run(filename)

    def getData(self):
        return self.data

    def __run(self, filename):
        """Reads text file"""
        f = open(filename, "r")
        contents = f.readlines()
        for line in contents:
            line = line.rstrip()
            if not (line == "ON" or line == "OFF"):
                print(line)
                xyz = line.split(",")
                point = Point(xyz[0].rstrip(), xyz[1].rstrip(), xyz[2].rstrip())
                self.data.append(point)
            else:
                self.data.append(line)
        f.close()
