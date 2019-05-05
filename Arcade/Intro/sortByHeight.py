def sortByHeight(a):
    sorted_list = sorted(i for i in a if i != -1)
    result = []
    index_result = 0
    for element in a:
        if element == -1:
           result.append(element)
        else:
           result.append(sorted_list[index_result])
           index_result += 1
    return result
    
'''Some people are standing in a row in a park. 
There are trees between them which cannot be moved. 
Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 
People can be very tall!

Example
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].'''
