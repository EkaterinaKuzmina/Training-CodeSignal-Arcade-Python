def addBorder(picture):
    picture = ["*"*len(picture[0])]+picture+["*"*(len(picture[0]))]
    picture = ["*"+i+"*" for i in picture ]
    return picture

'''Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example
For
picture = ["abc",
           "ded"]
the output should be
addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]'''
