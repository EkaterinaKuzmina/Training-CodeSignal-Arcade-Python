def alphabeticShift(inputString):
       az = list('abcdefghijklmnopqrstuvwxyz')
       result = []
       for i in list(inputString):
              if i != 'z':
                     result.append(az[az.index(i)+1])
              else:
                     result.append('a')
       return ''.join(result)

'''Given a string, replace each of its character by the next one in the English alphabet (z would be replaced by a).

Example
For inputString = "crazy", the output should be
alphabeticShift(inputString) = "dsbaz".'''
