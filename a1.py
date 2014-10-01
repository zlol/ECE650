

# develop the core features first. And then create i/o. remember to use python2

class street:
    def __init__(self, street_name, street_coord):
        self.name = street_name
        self.coord = street_coord

class Line_Segment:
    def __init__(self, s, e):
        self.start = s
        self.end = e

class Edge:
    def __init__(self, n1, n2):
        self.node1 = n1
        self.node2 = n2

street_list = list()
line_list = list()

#Now the problem is: given a set of line segments, fidn all the intersections and related nodes/edges.

def intersect(line1, line2):
    a1 = (line1.end[1] - line1.start[1])
    b1 = line1.start[0] - line1.end[0]
    c1 = a1 * line1.start[0] + b1*line1.start[1]

    a2 = line2.end[1] - line2.start[1]
    b2 = line2.start[0] - line2.end[0]
    c2 = a2 * line2.start[0] + b2 * line2.start[1]

    delta = a1*b2 - a2*b1
    #print("a1 ",a1, "a2 ", a2, "b1 ",b1, "b2 ", b2)
    if delta == 0:
        return None
    
    x = (b2*c1 - b1*c2)/delta
    y = (a1*c2 - a2*c1)/delta
    edge_list = list()
    node_list = list()

    if line1.start[0]<=x <=line1.end[0] and line1.start[1] <= y <=line1.end[1] and line2.start[0] <= x <= line2.end[0] and line2.start[1] <= y <= line2.end[1]:
        """
        for point in [(line1.start[0], line1.start[1]), (line1.end[0], line1.end[1]),
                      (line2.start[0], line2.start[1]), (line2.end[0], line2.end[2])]:
            if (x,y) != point:
        """     
        return (x,y)
    else:
        return None

#test the intersect function, critical
line1 = Line_Segment((0,0),(5,5))
line2 = Line_Segment((1,1),(5,1))

print(intersect(line1,line2))

def gen_graph(line1, line2, intersect):
    edgeList = list()
    nodeList = [intersect]
    for point in [(line1.start[0], line1.start[1]), (line1.end[0], line1.end[1]),
                    (line2.start[0], line2.start[1]), (line2.end[0], line2.end[2])]:
        if (x,y) != point:
            edgeList.add(Edge((x,y),point))
            nodeList.add(point)
    return [nodeList, edgeList]
