from SliceVis.txtreader import TxtReader
from SLiceVis.vis_geometry import *

class Visualizer(object):

    def __init__(self):
        self.data = []

    def load(self, toolpath_file):
        self.toolpath = toolpath_file
        self.points = TxtReader(self.toolpath)
        self.lines = segment(self.points)

    def segment(self, points):
        edges = []
        p1 = None
        p2 = None
        color = None
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
                        p1 = None
                        p2 = None
            else:
                if p1 is not None and (points(i) is not "ON" and points(i) is not "OFF"):
                    xyz = points(i).split(",")
                    p2 = Point(xyz[0], xyz[1], xyz[2])
                    edge = Line(p1, p2, color)
                    edges.append(edge)
        return edges

