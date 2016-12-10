#!/usr/bin/env python
# Jordan Bergero
# Fern Vue

class Node:
    def __init__(self, v):
        if(v == 'a'):
            self.a = 1
        else:
            self.a = 0
        if(v == 'b'):
            self.b = 1
        else:
            self.b = 0
        if(v == 'c'):
            self.c = 1
        else:
            self.c = 0
    def product(self, other):
        if(self.a == 1 and other.c == 1):
            a1 = 1
        if(self.b == 1 and other.c == 1):
            a1 = 1
        if(self.c == 1 and other.a == 1):
            a1 = 1
        if(self.a == 1 and  other.a == 1 or self.a == 1 and other.b == 1):
            b1 = 1
        if(self.b == 1 and other.b == 1):
            b1 = 1
        if(self.b == 1 and other.a == 1):
            c1 = 1
        if(self.c == 1 and other.b == 1 or self.c == 1 and other.c == 1):
            c1 = 1
        return Node(a1, b1, c1)
    def __str__(self):
        return "(a: {0},b: {1}, c: {2}".format(self.a, self.b,self.c)

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

def dynamic(sequence):
    l = list(sequence)
    print(len(l))
    node_array = [[0 for x in range(len(l))] for y in range(len(l))]
    for i in range (len(l)):
    #    print i
        node_array[0][i] = Node(l[i])
    return node_array
'''
    for k in range (1, len(l)):
        for i in range(1, len(l)-k + 1):
            for j in range (i, i + k - 2):
                v1 = node_array[i:j-i+1]
                v2 = node_array[j+1:k-j+i-1]
                node_array = product(v1,v2)
'''

def main():
    x = "abba"
    y = dynamic(x)
    for i in range(len(y)):
        print y[0][i]
main()
