def isLucky(n):
    k = len(str(n))
    first_part=0
    second_part=0
    n = str(n)
    for i in range(k//2):
        first_part += int(n[i])    
    for j in range(k//2, k):
        second_part += int(n[j])   
    return first_part==second_part

'''Ticket numbers usually consist of an even number of digits. 
A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example
For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.'''
