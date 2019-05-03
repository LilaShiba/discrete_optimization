############### start solution here #######################################
    table = [[0 for col in range(capacity+1)] for row in range(item_count)]
    for row in range(item_count):
        for col in range(capacity+1):
            if items[row].weight > col:
                table[row][col] = table[row-1][col]
                #print(items[row].weight)
            else:
                table[row][col] = max(table[row-1][col], table[row-1][col-items[row].weight] + items[row].value)
    value = table[-1][-1]

############### end solution here #######################################
