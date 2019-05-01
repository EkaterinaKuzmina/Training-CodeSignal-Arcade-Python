import numpy as np
def matrixElementsSum(matrix):
    x,y = np.shape(matrix)
    new_matrix = matrix
    for i in range(0, x-1):
        for j in range(0,y):
            if matrix[i][j] == 0:
                new_matrix[i][j] = 0
                for g in range(i+1,x):
                    new_matrix[g][j]= 0
    return sum(sum(new_matrix,[]))

'''After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! 
Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.
Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, 
your task is to return the total sum of all rooms that are suitable for the CodeBots 
(ie: add up all the values that don't appear below a 0).

Example
For
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.'''
