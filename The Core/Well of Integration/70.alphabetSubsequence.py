def alphabetSubsequence(s):
    az = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)-1):
        if az.index(s[i]) >= az.index(s[i+1]):
            return False
    return True

'''Check whether the given string is a subsequence of the plaintext alphabet.

Example
For s = "effg", the output should be
alphabetSubsequence(s) = false;
For s = "cdce", the output should be
alphabetSubsequence(s) = false;
For s = "ace", the output should be
alphabetSubsequence(s) = true;
For s = "bxz", the output should be
alphabetSubsequence(s) = true.'''
