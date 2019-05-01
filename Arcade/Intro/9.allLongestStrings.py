def allLongestStrings(inputArray):
    n = len(inputArray)
    temp_list = []
    max_len = max([len(i) for i in inputArray])
    for i in range(n):
        if len(inputArray[i]) == max_len:
            temp_list.append(inputArray[i])
    return temp_list

'''Given an array of strings, return another array containing all of its longest strings.

Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].'''
