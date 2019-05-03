#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    ############### start solution here #######################################
    # DP Solution slow is K is large

    table = [[0 for col in range(capacity+1)] for row in range(item_count)]
    for row in range(item_count):
        for col in range(capacity+1):
            if items[row].weight > col:
                table[row][col] = table[row-1][col]
                #print(items[row].weight)
            else:
                table[row][col] = max(table[row-1][col], table[row-1][col-items[row].weight] + items[row].value)
    value = table[-1][-1]
    # amount = value
    #
    # # backwards loop
    # # start,stop,step
    col = capacity
    for row in range(item_count-1,-1,-1):
        if row == 0 and table[row][col] != 0:
            taken[items[row].index] = 1
        if table[row][col] != table[row-1][col]:
            taken[items[row].index] = 1
            col -= items[row].weight



    ############### end solution here #######################################
    # greedy algorithm
    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
