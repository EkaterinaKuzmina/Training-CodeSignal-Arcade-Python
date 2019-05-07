def palindromeRearranging(inputString):
    from collections import Counter
    result = []
    d = Counter(inputString) 
    for i in d.values():
        result.append(i%2==0)
    return len(result) - sum(result) <= 1

'''Given a string, find out if its characters can be rearranged to form a palindrome.

Example
For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.'''
