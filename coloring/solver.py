#!/usr/bin/python
# -*- coding: utf-8 -*-
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


    def easy_solve():
        graph = {}
        # make adj_list
        # these are the constraints
        for x in range(edge_count):
            if edges[x][0] not in graph:
                graph[edges[x][0]] = [edges[x][1]]
            else:
                graph[edges[x][0]].append(edges[x][1])
        #print(graph)

        # sort by valency of value
        keys_valency = sorted(graph, key=lambda k: len(graph[k]), reverse = True)
        print(keys_valency)

        available = [0] * edge_count
        color_value = {}
        # for node in graph:
        #     neighbor_color =


    easy_solve()
    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
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
