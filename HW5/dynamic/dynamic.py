#!/usr/bin/env python
# Jordan Bergero
# Fern Vue
import copy

class Node:
    def __init__(self, v):
        self.a = 0
        self.b = 0
        self.c = 0
        if(v == 'a'):
            self.a = 1
        if(v == 'b'):
            self.b = 1
        if(v == 'c'):
            self.c = 1
    def addA(self):
        self.a = 1
    def addB(self):
        self.b = 1
    def addC(self):
        self.c = 1
    def product(self, other):
        N = Node('x')
        if(self.a == 1 and other.c == 1):
            N.addA()
        if(self.b == 1 and other.c == 1):
            N.addA()
        if(self.c == 1 and other.a == 1):
            N.addA()
        if(self.a == 1 and  other.a == 1 or self.a == 1 and other.b == 1):
            N.addB()
        if(self.b == 1 and other.b == 1):
            N.addB()
        if(self.b == 1 and other.a == 1):
            N.addC()
        if(self.c == 1 and other.b == 1 or self.c == 1 and other.c == 1):
            N.addC()
        return N
    def __str__(self):
        return "(a: {0},b: {1}, c: {2}".format(self.a, self.b,self.c)

def dynamic(sequence):
    l = list(sequence)
    node_array = [[0 for x in range(len(l))] for y in range(len(l))]
    for i in range (len(l)):
        node_array[0][i] = Node(l[i])

    for k in range (1,len(l)):
        for i in range(len(l) - k):
            v1 = node_array[k-1][i]
            v2 = node_array[k-1][i+1]
            node_array[k][i] = v1.product(v2)
    return node_array

def printArray (array):
    for i in range(len(array)):
        for j in range(len(array)-i):
            print(array[i][j])
        print "--------------"

def isA(array):
    for i in range(len(array)):
        for j in range(len(array)-i):
            n = array[i][j]
    if(n.a == 1 and n.b == 0 and n.c == 0):
        return "Yes."
    else:
        return "No."

def main():
    x = raw_input("Insert a string for the algorithm: ");
    y = dynamic(x)
    printArray(y)
    print(isA(y))

main()
