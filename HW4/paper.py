#!/usr/bin/env python
# Fern Vue
# Jordan Bergero

class Node:
    def __init__(self, a2, a3, a4, a5, cuts):
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.cuts = cuts
    def __ne__(self, other):
        return (self.a2 == other.a2) and (self.a3 == other.a3) and \
            (self.a4 == other.a4) and (self.a5 == other.a5)
    def __str__(self):
        return "({0},{1},{2},{3},{4})".format(self.a2, self.a3, self.a4, self.a5,self.cuts)
    def cut(node, piece):
        if(piece == 0 and node.a2 != 0):
            a2 = node.a2 - 1
            a3 = node.a3 + 1
            a4 = node.a4 + 1
            a5 = node.a5 + 1
            cuts = node.cuts + 1
        elif(piece == 1 and node.a3 != 0):
            a2 = node.a2
            a3 = node.a3 - 1
            a4 = node.a4 + 1
            a5 = node.a5 + 1
            cuts = node.cuts + 1
        else:
            a2 = node.a2
            a3 = node.a3
            a4 = node.a4 - 1
            a5 = node.a5 + 1
            cuts = node.cuts + 1
        return Node(a2,a3,a4,a5,cuts)

a = Node(1,1,1,2,0)
graph = {a:[a.cut(i) for i in range(3)]}
for k,v in graph.items():
    for i in v:
        graph.update({i : [i.cut(k) for k in range(3)]})

for k,v in graph.items():
    print "Parent Node: ", k
    print "Connected Nodes:"
    for i in v:
        print i

