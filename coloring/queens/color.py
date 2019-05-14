
    matrix = [[0 for x in range(0,node_count)] for y in range(0,node_count)]
    for x,y in edges:
        matrix[x][y] = 1
        matrix[y][x] = 1

    col_val = [None] * node_count

############### Backtracking Start #############################
    def printSolution(board):
        pprint.pprint(board)

    def isSafe(node,c):
        # iterate through all nodes in graph
        for i in range(node_count):
            # if adj node has same color, return false
            if matrix[node][i] == 1 and c == col_val[i]:
                return False
        return True

    def color(node,col_val):
        if node == node_count:
            return True

        for i in range(0,node_count-1):
            if isSafe(node,i):
                col_val[node] = i
                if color(node+1,col_val) == True:
                    return True
        return False




    ans = color(0,col_val)
    #printSolution(col_val)
    #print(ans)
    nc = max(col_val) + 1
    solution = col_val


# ############### Greedy end ###############################
#
#     matrix = [[0 for x in range(0,node_count)] for y in range(0,node_count)]
#     for x,y in edges:
#         matrix[x][y] = 1
#         matrix[y][x] = 1
#
#
#
#     col_val = [0] * node_count
#
# ############### Backtracking Start #############################
#     def printSolution(board):
#         pprint.pprint(board)
#
#     def isSafe(node,c):
#         # iterate through all nodes in graph
#         for i in range(node_count-1,0,-1):
#             # if adj node has same color, return false
#             if i != node:
#                 if matrix[node][i] == 1 and c == col_val[i]:
#                     return False
#         return True
#
#     def color(node,col_val):
#         if node == node_count:
#             return True
#
#         for i in range(magic):
#             if isSafe(node,i):
#                 col_val[node] = i
#                 if color(node+1,col_val) == True:
#                     return True
#         return False
#
#
#     magic = 100
#     # ans = True
#     # magic = 23
#     # while ans == True:
#     #     magic -= 1
#     ans = color(0,col_val)
#     print(ans)
#     #     if ans == False:
#     #         break
#     past_val = col_val
#     pnc = max(col_val)+1
#
#
#     #printSolution(col_val)
#
#     pnc = max(col_val) + 1
#     solution = past_val
