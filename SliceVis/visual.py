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
        for i in range(len(points)):
            if i != len(points)-1:
