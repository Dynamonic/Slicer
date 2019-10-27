from point import Point
from edge import Edge


class Shape(object):
    MAX_X = 250  # USED FOR INTERSECTION ALGORITHM
    MAX_Y = 250

    def __init__(self, data):
        self.points = data
        self.edges = []
        self._gen_edges(self.points)

    def _gen_edges(self, lop):
        """generates a list of edges: edges are two connected points"""
        for i in range(len(lop)):
            if i != len(lop)-1:
                edge = Edge(lop[i], lop[i+1])
                self.edges.append(edge)

    def get_edges(self):
        return self.edges

    def get_points(self):
        return self.points

    def get_size(self):
        # [min x, max x, min y, max y]
        vals = [10000, 0, 10000, 0]
        for point in self.points:
            if float(point.x) < float(vals[0]):
                vals[0] = point.x
            if float(point.x) > float(vals[1]):
                vals[1] = point.x
            if float(point.y) < float(vals[2]):
                vals[2] = point.y
            if float(point.y) > float(vals[3]):
                vals[3] = point.y
        return vals

    def in_shape(self, point):
        """determines if a given point lies inside the Shape object
        (note: a point lies inside a shape if a line extended to infinity in any direction
        from the point intersects with an odd number of the Shape's edges"""
        x = point.x
        y = point.y
        z = point.z
        x2 = point.x + self.MAX_X
        y2 = point.y
        z2 = point.z
        x3 = point.x
        y3 = point.y + self.MAX_Y
        z3 = point.z
        p1 = Point(x, y, z)
        # Create edge that is the point extended out to "infinity" in the X+ direction
        p2 = Point(x2, y2, z2)
        # Create edge that is the point extended out to "infinity" in the Y+ direction
        p3 = Point(x3, y3, z3)
        # if the point lies on one of the shapes edges then it is in the shape
        for edge in self.edges:
            if edge.point_on_line(p1):
                return True
        # end point check
        # Count the number of times that the extended line intersects with the edges of the shape
        count1 = 0
        count2 = 0
        for edge in self.edges:
            if self._intersect(edge, Edge(p1, p2)):
                count1 += 1
            if self._intersect(edge, Edge(p1, p3)):
                count2 +=1
        if count1 == count2 and count1 % 2 == 1:
            return True
        elif count1 != count2:  # helps prevent errors with counting points between edges
            return True
        return False

    def _intersect(self, line1, line2):
        """determines if two lines intersect
        line: [point1, point2]"""
        # if either line has no length check if the point lies on the other line
        if line1.line_length() == 0:
            return line2.point_on_line(line1.point1)
        if line2.line_length() == 0:
            return line1.point_on_line(line2.point1)
        # check if endpoints of the line lie on the line (colinear)
        if line2.point_on_line(line1.point1):
            return True
        if line2.point_on_line(line1.point2):
            return True
        if line1.point_on_line(line2.point1):
            return True
        if line1.point_on_line(line2.point2):
            return True
        # Check if line segments are parallel
        s1 = line1.slope()
        s2 = line2.slope()
        if s1 == s2:
            return False
        # End Parallel check
        # Calculates intersect point assuming segments are lines
        if s1 is not None and s2 is not None:
            # Solve linear eqns
            b1 = float(line1.y_intercept())
            b2 = float(line2.y_intercept())
            if s1 != s2:
                x = (b2-b1)/(s1-s2)
                y = s1 * x + b1
            else:
                return False
        elif s1 is not None:
            # this means s2 has one x value
            x = line2.point1.x
            y = s1 * x + line1.y_intercept()
        else:  # s1 has one x value
            x = line1.point1.x
            y = s2 * x + line2.y_intercept()
        # Line segment stuff:
        # this checks the interval that would have the intersection
        # if calculated x and y are in the interval then the SEGMENTS intersect at point (x,y)
        x_vals = [line1.point1.x, line1.point2.x, line2.point1.x, line2.point2.x]
        y_vals = [line1.point1.y, line1.point2.y, line2.point1.y, line2.point2.y]
        x_vals.sort()
        y_vals.sort()
        x_int = [x_vals[1], x_vals[2]]
        y_int = [y_vals[1], y_vals[2]]
        if min(x_int) <= x <= max(x_int) and min(y_int) <= y <= max(y_int):
            return True
        else:
            return False
