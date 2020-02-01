# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 07:49:01 2020

@author: User
"""
import array as arr
input ="The sunset sets at twelve o'clock"

def alphabet_position(input):
    alphabet = ""
    input = input.lower()
    a=arr.array('b')
    for character in input:
        if character != ' ':
            number = ord(character) - 96
            if 0<number<=26:
                a.extend([number])

    for digit in a:
        alphabet += str(digit)
        alphabet += ' '   
    return alphabet.strip()

alphabet=alphabet_position(input)
print(alphabet)

