from SliceTest.readSlice import SliceReader
from SliceTest.shape import Shape
from SliceTest.point import Point


class Toolpath(object):
    """Toolpath object takes a file name and bead size to make toolpath slices out of slice geometries"""
    DEFAULT_BEAD = 1
    in_data = []
    out_data = []
    DEFAULT_OUT = "default_out.txt"

    def __init__(self, out_file=DEFAULT_OUT, bead=DEFAULT_BEAD):
        self.bead_thickness = bead
        self.outfile = out_file
        slice = SliceReader()
        self.in_data = slice.getData()

    def raster(self):
        """Algorithm that makes tool paths by going back and forth"""
        # Dumb algorithm, works like a print head
        self.out_data.clear()
        shape = Shape(self.in_data)
        vals = shape.get_size()
        x_interval = [vals[0], vals[1]]
        y_interval = [vals[2], vals[3]]
        prev_state = None
        for y in range(int(y_interval[0]), int(y_interval[1])+1, 2):
            x = int(x_interval[0])
            self.out_data.append(Point(x, y))
            for x in range(int(x_interval[0]), int(x_interval[1])+1):
                point = Point(x, y)
                in_shape = shape.in_shape(point)
                if (in_shape != prev_state) and in_shape:
                    prev_state = True
                    self.out_data.append(point)
                    self.out_data.append("ON")
                elif (in_shape != prev_state) and not in_shape:
                    prev_state = False
                    self.out_data.append(point)
                    self.out_data.append("OFF")
            self.out_data.append(Point(x, y))
            y += 1
            self.out_data.append(Point(x, y))
            for x in range(int(x_interval[1]), int(x_interval[0])-1, -1):
                point = Point(x, y)
                in_shape = shape.in_shape(point)
                if (in_shape != prev_state) and in_shape:
                    prev_state = True
                    self.out_data.append(point)
                    self.out_data.append("ON")
                elif (in_shape != prev_state) and not in_shape:
                    prev_state = False
                    self.out_data.append(point)
                    self.out_data.append("OFF")
            self.out_data.append(Point(x, y))
        self.send(self.out_data)

    def contour(self):
        """Algorithm that creates toolpath that spirals inward while staying parallel to closest outside edge"""
        return None
        # ADD CODE

    def hybrid(self):
        """Algorithm that creates outer edges with contour and then rasters inside"""
        return None
        # ADD CODE

    def send(self, out_data, out_file=DEFAULT_OUT):
        """Writes the toolpath to a text file"""
        f = open(out_file, "w")
        for point in out_data:
            if type(point) is str:
                f.write(point + "\n")
            else:
                f.write(point.point_str() + "\n")
        f.close()


def test():
    testing = Toolpath()
    testing.raster()

if __name__ == "__main__":
    test()

