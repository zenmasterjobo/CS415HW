#!/usr/bin/env python
# Fern Vue
# Jordan Bergero

import sys

count = 0
sys.setrecursionlimit(100000000)
class Node:
    def __init__(self, a2, a3, a4, a5, cuts):
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.cuts = cuts
        self.children = []
    def __ne__(self, other):
        return not self.__eq__(other)
    def __eq__(self, other):
        return (self.a2 == other.a2) and (self.a3 == other.a3) and \
            (self.a4 == other.a4) and (self.a5 == other.a5) and (self.cuts == other.cuts)
    def __str__(self):
        return "({0},{1},{2},{3},{4})".format(self.a2, self.a3, self.a4, self.a5,self.cuts)
    def grab(node):

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
        x = Node(a2,a3,a4,a5,cuts)
        if(x != node):
            node.children.append(x)
        
        if(node.a3 != 0):
            a2 = node.a2
            a3 = node.a3 - 1
            a4 = node.a4 + 1
            a5 = node.a5 + 1
            cuts = node.cuts + 1
        else:
            a2 = node.a2
            a3 = node.a3
            a4 = node.a4
            a5 = node.a5
            cuts = node.cuts
        x = Node(a2,a3,a4,a5,cuts)
        if(x != node):
            node.children.append(x)

        if(node.a4 != 0):
            a2 = node.a2
            a3 = node.a3
            a4 = node.a4 - 1
            a5 = node.a5 + 1
            cuts = node.cuts + 1
        else:
            a2 = node.a2
            a3 = node.a3
            a4 = node.a4
            a5 = node.a5
            cuts = node.cuts
        x = Node(a2,a3,a4,a5,cuts)
        if(x != node):
            node.children.append(x)

        if(node.finish()):
            node.children.append(Node(0,0,0,1,node.cuts))
        else:
            a2 = node.a2
            a3 = node.a3
            a4 = node.a4
            a5 = node.a5 - 1
            cuts = node.cuts
            x = Node(a2,a3,a4,a5,cuts)
            if(x != node and a5 != 0):
                node.children.append(x)

    def finish(self):
        return (self.a2 == 0 and self.a3 == 0 and self.a4 == 0 and self.a5 == 1)
    
    def graphGen(self):
        if (self.finish()):
            return
        self.grab()
        for i in self.children:
            i.graphGen()

    def printGraph(self):
        global count
        count += 1
        if (self.finish()):
            print self
            return
        print self
        for i in self.children:
            i.printGraph()

    def printWorstCase(self):
        if (self.finish()):
            print self
            return 1
        print self
        for i in self.children:
            return 1 + i.printWorstCase()


a = Node(1,1,1,2,0)
a.graphGen()
a.printGraph()
print "Number of children (With Repeats)",count
print "Expected Number of cuts (Worst Case) "
print a.printWorstCase()
