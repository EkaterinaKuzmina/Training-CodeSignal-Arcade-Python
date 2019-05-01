from collections import Counter

def commonCharacterCount(s1, s2):
    common_letters = dict(Counter(s1) & Counter(s2)) 
    common_counts = list(common_letters.values())
    result = sum(common_counts)
    return result

'''Given two strings, find the number of common characters between them.

Example
For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c".'''
