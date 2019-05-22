#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=miCYGGrTwFU
from collections import Counter
import pprint

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))


    # build a trivial solution
    # every node has its own color
    solution = range(0, node_count)


############### Backtracking Start #############################
    #
    #
    # matrix = [[0 for x in range(0,node_count)] for y in range(0,node_count)]
    # for x,y in edges:
    #     matrix[x][y] = 1
    #     matrix[y][x] = 1
    #
    # # def printSolution(board):
    # #     pprint.pprint(board)
    # #
    # def isSafe(node,c, col_val):
    #     # iterate through all nodes in graph
    #     for i in range(0,node_count):
    #         # if adj node has same color, return false
    #         if i != node:
    #             if matrix[node][i] == 1 and c == col_val[i]:
    #                 return False
    #     return True
    # #
    # def colorUtl(node, magic, col_val):
    #     #col_val = sorted(col_val, key = col_val.count)
    #
    #
    #
    #     if node == node_count:
    #         return True
    #
    #     for c in range(1,magic):
    #         if isSafe(node, c, col_val):
    #             # try from most used number to least used number
    #             col_val[node] = c
    #             if colorUtl(node+1, magic, col_val) == True:
    #                 return True
    #             col_val[node] = 0
    #
    # def color(magic):
    #     col_val = [0] * node_count
    #     if colorUtl(0,magic,col_val) == False:
    #         return False
    #     return col_val
    # #
    # #
    # #
    # #
    # colors = color(node_count)
    # colors = color(max(colors)-1)
    # #
    # #
    # # #printSolution(col_val)
    # #
    # nc = max(colors)
    # print(nc)
    # solution = colors


############### Backtracking End ##############################
    # colors = [x+1 for x in range(node_count)]
    #
    def make_adj_list():
        adj_list = {}
        for x in range(0,node_count):
            adj_list[x] = []
        for x,y in edges:
            adj_list[x].append(y)
        return adj_list




    matrix = [[0 for x in range(0,node_count)] for y in range(0,node_count)]
    for x,y in edges:
        matrix[x][y] = 1
        matrix[y][x] = 1



    # ### work on
    def isSafe(node,color,color_of_edges):

        for i in range(0,node_count):
            # if adj node has same color, return false
            if i != node:
                if matrix[node][i] == 1 and color == color_of_edges[i]:
                    return False
        return True
    #
    def get_edge_color(node,color_of_edges):
        # make max list here
        for color in range(0,node_count-1):
            if isSafe(node,color,color_of_edges):
                return color
    #
    def main(color_of_edges):
        for node in sorted_adj_list:
            color_of_edges[node] = get_edge_color(node,color_of_edges)
        return color_of_edges
    #
    adj_list = make_adj_list()
    sorted_adj_list = sorted(adj_list, key=lambda edge: len(adj_list[edge]), reverse = True)
    ce = {}
    for x in range(0,node_count):
        ce[x] = x
    ans = main(ce)
    solution = []
    for key, value in ans.items():
        solution.append(value)


############### Local Search Start ############################
    # return values
    nc = max(solution)+1




############### Local Search End ############################



    # prepare the solution in the specified output format
    output_data = str(nc) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')
