#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    for item in items 
      val = []

      
    Item.size
    Item.value

    pass

# def knapSack(W, wt, val, n):
#    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
#    #Table in bottom up manner
#    for i in range(n + 1):
#       for w in range(W + 1):
#          if i == 0 or w == 0:
#             K[i][w] = 0
#          elif wt[i-1] <= w:
#             K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
#          else:
#             K[i][w] = K[i-1][w]
#    return K[n][W]
# #Main
# val = [50,100,150,200]
# wt = [8,16,32,40]
# W = 64
# n = len(val)
# print(knapSack(W, wt, val, n))

# def knapSack(weight_threshold, weight_list, util_list): 
#     """ 
#     A Dynamic Programming algorithm that solves the 0-1 Knapsack problem.
#     Args:
#         weight_threshold: Weight threshold
#         weight_list: List of weights for each item in item set I
#         util_list: utility score of each item i
#     Returns:
#         The optimal utility score of the knapsack problem
#     """
#     n = len(util_list)
#     lookup_table = [[0 for x in range(weight_threshold+1)] 
#                     for x in range(n+1)] 
  
#     # Build table K[][] in bottom up manner 
#     for i in range(n+1): 
#         for w in range(weight_threshold+1): 
#             if i==0 or w==0: 
#                 lookup_table[i][w] = 0
#             elif weight_list[i-1] <= w:
#                 lookup_table[i][w] = (
#                     max(util_list[i-1] 
#                         + lookup_table[i-1][w-weight_list[i-1]], 
#                         lookup_table[i-1][w]))
#             else: 
#                 lookup_table[i][w] = (
#                     lookup_table[i-1][weight_threshold])
  
#     return lookup_table[n][weight_threshold]


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')