"""
File: Heaviside.py

Copyright (c) 2016 Rachel Benavente

License: MIT

This code defines a function and tests to see if the function accurately works.
"""

#a
def H(x):
    if x < 0:
        value = 0
    if x >= 0:
        value = 1
    return value

#b
def test_H():
    if H(-10) != 0:
        print "Error"
    elif H(-10**-15) != 0:
        print "Error"
    elif H(10**-15) != 1:
        print "Error"
    elif H(10) != 1:
        print "Error"
    else:
        print "Everything is good!"

test_H()
