from SliceVis.txtreader import TxtReader
from SLiceVis.vis_geometry import *
import matplotlib as plt

class Visualizer(object):

    def __init__(self):
        self.data = []

    def load(self, toolpath_file):
        self.toolpath = toolpath_file
        self.points = TxtReader(self.toolpath)
        self.lines = self.segment(self.points)

    def segment(self, points):
        edges = []
        p1 = None
        p2 = None
        color = 0
        for i in range(len(points)):
            if i != len(points)-1:
                if points(i) is "ON":
                    color = 1
                elif points(i) is "OFF":
                    color = 2
                else:
                    if p1 is None:
                        xyz = points(i).split(",")
                        p1 = Point(xyz[0], xyz[1], xyz[2])
                    else:
                        xyz = points(i).split(",")
                        p2 = Point(xyz[0], xyz[1], xyz[2])
                        edge = Line(p1, p2, color)
                        edges.append(edge)
                        p1 = p2
                        p2 = None
            else:
                if p1 is not None and (points(i) is not "ON" and points(i) is not "OFF"):
                    xyz = points(i).split(",")
                    p2 = Point(xyz[0], xyz[1], xyz[2])
                    edge = Line(p1, p2, color)
                    edges.append(edge)
        return edges

    def display(self, lines):
        fig, ax = plt.subplots()
        for line in lines:
            if line.color == 0:
                color = 'g'
            elif line.color == 1:
                color = 'r'
            elif line.color == 2:
                color = 'b'
            else:
                color = 'c'
            ax.add_line(lines.Line2D(line.get_xs(), line.get_ys(), linewidth=2, color=color))
        plt.plot()
        plt.show()

