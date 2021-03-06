#!/usr/bin/env python
# Fern Vue
# Jordan Bergero

class Node:
    def __init__(self, a2, a3, a4, a5, cuts,children):
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.cuts = cuts
        self.children = children
    def __ne__(self, other):
        return (self.a2 == other.a2) and (self.a3 == other.a3) and \
            (self.a4 == other.a4) and (self.a5 == other.a5)
    def __str__(self):
        return "({0},{1},{2},{3},{4})".format(self.a2, self.a3, self.a4, self.a5,self.cuts)
    def grab(node, piece):
        if (node.finish()):
            return Node(node.a2,node.a3,node.a4.node.a5,node.cuts,node.children)
        elif(piece == 0):
            if(node.a2 != 0):
                a2 = node.a2 - 1
                a3 = node.a3 + 1
                a4 = node.a4 + 1
                a5 = node.a5 + 1
                cuts = node.cuts + 1
            else:
                a2 = node.a2
                a3 = node.a3
                a4 = node.a4
                a5 = node.a5
                cuts = node.cuts
        elif(piece == 1):
            a2 = node.a2
            if(node.a3 != 0):
                a3 = node.a3 - 1
                a4 = node.a4 + 1
                a5 = node.a5 + 1
                cuts = node.cuts + 1
            else:
                a3 = node.a3
                a4 = node.a4
                a5 = node.a5
                cuts = node.cuts
        elif (piece == 2):
            a2 = node.a2
            a3 = node.a3
            if(node.a4 != 0):
                a4 = node.a4 - 1
                a5 = node.a5 + 1
                cuts = node.cuts + 1
            else:
                a4 = node.a4
                a5 = node.a5
                cuts = node.cuts
        else:
            a2 = node.a2
            a3 = node.a3
            a4 = node.a4
            a5 = node.a5 - 1
            cuts = node.cuts
        return Node(a2,a3,a4,a5,cuts)
    def finish(self):
        return (self.a2 == 0 and self.a3 == 0 and self.a4 == 0 and self.a5 == 1)
    def search(node):
        if(self.a2 == 0)
            search(Node(node
        if(self.a3 == 0)
            search(Node(node
        if(self.a4 == 0)
            search(Node(node
        if(self.a5 == 0)
            search(Node(node
    
    
a = Node(1,1,1,2,0)

graph = {a:[a.grab(i) for i in range(4)]}

#for k,v in graph.items():
#    for i in v:
#        graph.update({i : [i.grab(j) for j in range(4)]})

for k,v in graph.items():
    print "Parent Node: ", k
    print "Connected Nodes:"
    for i in v:
        print i

