#!/usr/bin/python
# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=miCYGGrTwFU
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

    #print(edges)

    # build a trivial solution
    # every node has its own color
    solution = range(0, node_count)
############### Greedy Start #############################
    # def greedy():
    #     graph = {}
    #     # make adj_list
    #     # these are the constraints
    #     for x in range(edge_count):
    #         if edges[x][0] not in graph:
    #             graph[edges[x][0]] = [edges[x][1]]
    #         else:
    #             graph[edges[x][0]].append(edges[x][1])
    #
    #     # sort by valency of value
    #     #keys_valency = sorted(graph, key=lambda k: len(graph[k]), reverse = True)
    #     #print(keys_valency)
    #
    #     #dictionary to store the colors assigned to each node
    #     col_val = {x:0 for x in range(node_count)}
    #
    #     count = 0
    #     colors = [0] * node_count
    #     for node in graph:
    #         for edge in graph[node]:
    #             if col_val[edge] == col_val[node]:
    #                 count +=1
    #                 col_val[edge] = count
    #
    #
    #
    #     # od = collections.OrderedDict(sorted(col_val.items()))
    #     # print(od)
    #     for x in col_val:
    #         colors[x] = col_val[x]
    #     #print(colors)
    #     #
    #     #
    #     num = max(colors) +1
    #     return colors, num
    #         # if solve(i) == True:
    #         #     return True
    #
    #

############### Greedy end ###############################

    matrix = [[0 for x in range(0,node_count)] for y in range(0,node_count)]
    for x,y in edges:
        matrix[x][y] = 1
        matrix[y][x] = 1

############### Backtracking Start #############################
    def printSolution(board):
        pprint.pprint(board)

    def isSafe(node,c, col_val):
        # iterate through all nodes in graph
        for i in range(0,node_count):
            # if adj node has same color, return false
            if i!= node:
                if matrix[node][i] == 1 and c == col_val[i]:
                    return False
        return True

    def colorUtl(node, magic, col_val):
        if node == node_count:
            return True

        for c in range(1,magic):
            if isSafe(node, c, col_val):
                col_val[node] = c
                if colorUtl(node+1, magic, col_val) == True:
                    return True
                col_val[node] = 0

    def color(magic):
        col_val = [0] * node_count
        if colorUtl(0,magic,col_val) == False:
            print(False)
            return False

        return col_val




    colors = color(node_count)


    #printSolution(col_val)

    nc = max(colors)
    print(nc)
    solution = colors


############### Backtracking End ##############################

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
