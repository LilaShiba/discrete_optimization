
    def isSafe(node, c):
        i = 0
        while i < edge_count:
            if matrix[node][i] == 1 and c == col_val[i]:
                return False
            i+=1
        return True

    def color(node):
        for c in range(1,node_count):
            if isSafe(node,c):
                col_val[node] = c
                if node+1 < edge_count:
                    color(node + 1)

        nc = len(set(col_val))
        return nc, col_val

    nc, solution = color(0)
