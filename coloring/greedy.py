    def easy_solve():
        graph = {}
        # make adj_list
        # these are the constraints
        for x in range(edge_count):
            if edges[x][0] not in graph:
                graph[edges[x][0]] = [edges[x][1]]
            else:
                graph[edges[x][0]].append(edges[x][1])

        # sort by valency of value
        #keys_valency = sorted(graph, key=lambda k: len(graph[k]), reverse = True)
        #print(keys_valency)

        #dictionary to store the colors assigned to each node
        col_val = {x:0 for x in range(node_count)}

        count = 0
        colors = [0] * node_count
        for node in graph:
            for edge in graph[node]:
                if col_val[edge] == col_val[node]:
                    count +=1
                    col_val[edge] = count



        # od = collections.OrderedDict(sorted(col_val.items()))
        # print(od)
        for x in col_val:
            colors[x] = col_val[x]
        #print(colors)
        #
        #
        num = max(colors) +1
        return colors, num
            # if solve(i) == True:
            #     return True


    solution, node_count = easy_solve()
