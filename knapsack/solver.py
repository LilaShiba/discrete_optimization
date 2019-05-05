#!/usr/bin/python
# -*- coding: utf-8 -*-
import pprint
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
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

    value = 0
    weight = 0
    taken = [0]*len(items)
############### start greedy here ################################################
    def greedy(items):
        length = len(items)
        weight_est = 0
        value_est = 0
        value_weight = namedtuple("value_weight", ['index', 'ratio', 'value', 'weight'])
            # sort by value/weight ratio and make it easy to access each property
        vw = []
        for i in range(length):
            vw.append(value_weight(items[i].index, items[i].value/items[i].weight, items[i].value, items[i].weight))
        vw.sort(key=lambda x: x[1], reverse=True)

        for obj in vw:
            if weight_est + obj.weight <= capacity:
                #taken[obj.index] = 1
                value_est += obj.value
                weight_est += obj.weight
                taken[obj.index] = 1
        return value_est, taken
############### start linear_relaxtion here #######################################
# linear_relaxtion
    # if item_count > 200:
    def linear_relaxtion(items):
        length = len(items)
        weight_est = 0
        value_est = 0
        value_weight = namedtuple("value_weight", ['index', 'ratio', 'value', 'weight'])

            # sort by value/weight ratio and make it easy to access each property
        vw = []
        for i in range(length):
            vw.append(value_weight(items[i].index, items[i].value/items[i].weight, items[i].value, items[i].weight))

        vw.sort(key=lambda x: x[1], reverse=True)
        ordered_list = vw.copy()


        for obj in vw:
            if weight + obj.weight <= capacity:
                #taken[obj.index] = 1
                value_est += obj.value
                weight_est += obj.weight
                vw.remove(obj)

        for fraction in vw:
            if weight + fraction.ratio <= capacity:
                value_est += fraction.ratio
                weight_est += fraction.ratio
        return value_est, ordered_list


############### end linear_relaxtion here #######################################
############### start DP solution here #########################################
    # DP Solution slow is K is large
    def dp(items):
        table = [[0 for col in range(capacity+1)] for row in range(item_count)]
        for row in range(item_count):
            for col in range(capacity+1):
                if items[row].weight > col:
                    table[row][col] = table[row-1][col]
                    #print(items[row].weight)
                else:
                    table[row][col] = max(table[row-1][col], table[row-1][col-items[row].weight] + items[row].value)
        value = table[-1][-1]
        # backwards loop
        # start,stop,step
        col = capacity
        for row in range(item_count-1,-1,-1):
            if row == 0 and table[row][col] != 0:
                taken[items[row].index] = 1
            if table[row][col] != table[row-1][col]:
                taken[items[row].index] = 1
                col -= items[row].weight
        return value,taken


############### end DP solution here #########################################

############### start BB solution here #######################################
    def bb(items):
        actual_value = 0
        best_solution = 0
        best_estimate = 0
        best_new_opt = 0
        # sorted list of value/weight
        opitmal_estimate,_ = linear_relaxtion(items)
        # root node of tree
        #nodes = []
        #nodes.append( (actual_value, capacity, best_estimate) )

        for x in range(len(items)):
            temp_opitmal_estimate = linear_relaxtion(items[x:])
            temp,takens = greedy(items[x:])

            if temp > best_solution:
                best_solution = temp
                taken = takens

            new_opt = opitmal_estimate - temp
            if new_opt > best_new_opt:
                best_new_opt = new_opt
            if new_opt < best_new_opt:
                break



        return best_solution, taken









############### end BB solution here #######################################

    if item_count <= 250:
        value, taken = dp(items)
        forsure = "1"
    elif item_count <= 400:
        _, o_items = linear_relaxtion(items)
        value, taken = bb(o_items)
        forsure = "0"
    else:
        value,take = greedy(items)
        forsure = "0"


    #value,taken = greedy(items)
    #print(bb(items))

    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + forsure + '\n'
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
