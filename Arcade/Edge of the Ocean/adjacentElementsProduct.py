def adjacentElementsProduct(inputArray):
    n = len(inputArray)
    maximum = -float("inf")
    for i in range(0, n-1):
        t = inputArray[i]*inputArray[i+1]
        if t > maximum:
            maximum = t
    return maximum

'''Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example
For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product.'''
