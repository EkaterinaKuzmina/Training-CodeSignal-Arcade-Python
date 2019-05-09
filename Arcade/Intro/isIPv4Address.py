def isIPv4Address(inputString):
     from collections import Counter
     count = Counter(inputString)
     if not all([c.isdigit() or c == '.' for c in inputString]):
          return False
     elif count['.'] == 3:
          dots = [i for i in range(len(inputString)) if inputString[i] =='.']
          part1 = inputString[:dots[0]]
          if len(part1) < 1:
               return False
          part2 = inputString[dots[0]+1:dots[1]]
          if len(part2) < 1:
               return False
          part3 = inputString[dots[1]+1:dots[2]]
          if len(part3) < 1:
               return False
          part4 = inputString[dots[2]+1:]
          if len(part4) < 1:
               return False   
          parts = [part1,part2,part3,part4]
          return all(int(part) in range(256) for part in parts)
     else:
          return False

'''An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. 
There are two versions of the Internet protocol, and thus two versions of addresses. 
One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;
For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.
316 is not in range [0, 255].
For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.
There is no first number.'''
