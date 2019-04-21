def adjacentElementsProduct(inputArray):
    n = len(inputArray)
    maximum = -float("inf")
    for i in range(0, n-1):
        t = inputArray[i]*inputArray[i+1]
        if t > maximum:
            maximum = t
    return maximum
