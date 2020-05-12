from SliceVis.txtreader import TxtReader
from SliceVis.vis_geometry import *
import matplotlib.pyplot as plt


class Visualizer(object):

    def __init__(self):
        self.data = []

    def load(self, toolpath_file):
        """Loads text file for reading"""
        self.toolpath = toolpath_file
        self.points = TxtReader(self.toolpath).getData()
        self.lines = self.segment()

    def run(self, type=1):
        if type == 1:
            self.display(self.lines)
        else:
            self.display_arrows(self.lines)

    def segment(self):
        """Takes list of points and turns them into a list of connected lines"""
        points = self.points
        edges = []
        p1 = None
        p2 = None
        color = 0
        for i in range(len(points)):
            if i != len(points)-1:
                if points[i] == "ON":
                    color = 1
                elif points[i] == "OFF":
                    color = 2
                else:
                    if p1 is None:
                        p1 = points[i]
                    else:
                        p2 = points[i]
                        edge = Line(p1, p2, color)
                        edges.append(edge)
                        p1 = p2
                        p2 = None
            else:
                if p1 is not None and (points[i] != "ON" and points[i] != "OFF"):
                    p2 = points[i]
                    edge = Line(p1, p2, color)
                    edges.append(edge)
        return edges

    @staticmethod
    def display(lines):
        fig = plt.figure()
        ax = plt.axes()
        ax.grid(linestyle=':')
        for line in lines:
            if line.color == 0:
                color = 'g'
            elif line.color == 1:
                color = 'r'
            elif line.color == 2:
                color = 'b'
            else:
                color = 'c'
            ax.add_line(plt.Line2D(line.get_xs(), line.get_ys(), linewidth=2, color=color))
        plt.plot()
        plt.show()

    @staticmethod
    def display_arrows(lines):
        fig = plt.figure()
        ax = plt.axes()
        ax.grid(linestyle=':')
        for line in lines:
            if line.color == 0:
                color = 'g'
            elif line.color == 1:
                color = 'r'
            elif line.color == 2:
                color = 'b'
            else:
                color = 'c'
            start = line.get_start()
            dist = line.xy_dist()
            ax.add_line(plt.arrow(start.get_x(), start.get_y(), dist[0], dist[1],
                                  width=.2, color=color))
        plt.plot()
        plt.show()

# BEGIN VISUALIZER TEST


def vis_test():
    vis = Visualizer()
    vis.load("vis_test.txt")
    vis.run(0)

if __name__ == "__main__":
    vis_test()