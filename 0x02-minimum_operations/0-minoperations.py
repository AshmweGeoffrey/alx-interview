#!/usr/bin/python3
"""" 
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

"""
def minOperations(n):
    """ Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6 """
    if not isinstance(n,int):
        return 0
    ops_count=0
    clipboard=1
    current=0
    while clipboard < n:
        if clipboard % 2 == 0:
            ops_count +=2
            clipboard += clipboard/2
            print('2.{}'.format(ops_count))
        else:
            ops_count +=1
            clipboard += clipboard
            print('1.{}'.format(ops_count))
    return ops_count
