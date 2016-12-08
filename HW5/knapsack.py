#!/usr/bin/env python
# Jordan Bergero
# Fern Vue

import sys

def knapsack(items, maxweight):
        bestvalues = [[0] * (maxweight + 1) for i in xrange(len(items) + 1)]

        for i, (value, weight) in enumerate(items):
            i += 1
            for capacity in xrange(maxweight + 1):
                if weight > capacity:
                    bestvalues[i][capacity] = bestvalues[i - 1][capacity]
                else:
                    trial1 = bestvalues[i - 1][capacity]
                    trial2 = bestvalues[i - 1][capacity - weight] + value
                    bestvalues[i][capacity] = max(trial1, trial2)
        reconstruction = []
        i = len(items)
        j = maxweight
        while i > 0:
            if bestvalues[i][j] != bestvalues[i - 1][j]:
                reconstruction.append(items[i - 1])
                j -= items[i - 1][1]
            i -= 1

        reconstruction.reverse()

        return bestvalues[len(items)][maxweight], reconstruction

def main():
    if len(sys.argv) != 2:
        print('usage: knapsack.py [file]')
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as file:
        lines = file.readlines()

    maxweight = int(lines[0])
    items = [map(int, line.split()) for line in lines[1:]]

    efficient, reconstruction = knapsack(items, maxweight)

    print ('Best value:', efficient)

    print('Items:')
    for value, weight in reconstruction:
        print('V: {0}, W: {1}'.format(value, weight))
    
main()
