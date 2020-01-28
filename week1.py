# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 07:49:01 2020

@author: User
"""
import array as arr
mystring = ""
input ="The sunset sets at twelve o'clock"
input = input.lower()
a=arr.array('b')
for character in input:
    if character != ' ':
        number = ord(character) - 96
        if 0<number<=26:
            a.extend([number])
            print(a)

for digit in a:
    mystring += str(digit)
    mystring += ' '
print(mystring)    

