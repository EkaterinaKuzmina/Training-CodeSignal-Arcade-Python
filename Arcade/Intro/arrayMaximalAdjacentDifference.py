def arrayMaximalAdjacentDifference(inputArray):
    new = []
    n = len(inputArray)
    for i in range(1, n):
        dif = abs(inputArray[i] - inputArray[i-1])
        new.append(dif)
    return sorted(new)[-1]
    
'''Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example
For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.'''
