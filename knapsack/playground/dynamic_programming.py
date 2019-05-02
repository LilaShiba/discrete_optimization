# I = {1,2...,n}
# O(k,j) is the optimal solution
# k = capacity
# j = items

# Assume we can solve all subproblems
# O(k,j-1) is the oracale

# first we try to add just one more item to the knapsack
# we can
# not add the item, and we get O(k, j-1)
# add the item, best solution is value of j + O(k-w,j-1)

# summary
# O(k,j) = max( O(k,j-1), vj + O(k-w,j-1)) if weight of j <= knapsack
# otherwise O(k,j) = O(k,j-1)
import pprint
def knapsack(maxWeight,items):

  matrix = [[0 for col in range(maxWeight+1)]for row in range(len(items[0]))]

  for row in range(len(items[0])):
    for col in range(maxWeight+1):
      if items[0][row] > col:
        matrix[row][col] = matrix[row-1][col]
      else:
        matrix[row][col] = max(matrix[row-1][col], matrix[row-1][col-items[0][row]]+items[1][row])
  # return matrix for max weight
  packed = []
  col = maxWeight
  # decrement loop
  for row in range(len(items[0])-1,-1,-1):
      if row == 0 and matrix[row][col] != 0:
        packed.insert(0,row)
      if matrix[row][col] != matrix[row-1][col]:
        packed.insert(0,row)
        col -= items[0][row]
  return matrix[len(items[0])-1][maxWeight]



def dp_knapsack(maxWeight,items):
    item_weight = items[0]
    print(item_weight)
    item_value = items[1]
    table = [[0 for x in range(maxWeight+1)] for y in range(len(item_weight))]
    # knapsack capacity
    #-1-2-3-4-5-6     i
    #------------     t
    #------------     e
    #------------     m
    #                 weight

    for row in range(len(item_weight)):
        for col in range(maxWeight+1):
            # if you can't add to the knapsack
            # value carry overs from previous measurement
            if item_weight[row] > col:
                table[row][col] = table[row-1][col]
            else:
                # [col-items[0][row]]+items[1][row]
                table[row][col] = max(table[row-1][col], table[row-1][col-item_weight[row]] + item_value[row])
    return table[-1][-1]

def knapSack(W , wt , val , n):

    # Base Case
    if n == 0 or W == 0 :
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
                   knapSack(W , wt , val , n-1))

val = [7,2,4,5]
wt = [3,1,2,4]
W = 6
n = len(val)

itemWeight = [3,1,2,4]
itemValues = [7,2,4,5]
items = [itemWeight,itemValues]

pprint.pprint(dp_knapsack(6,items))
print(knapSack(W,wt,val,n))
