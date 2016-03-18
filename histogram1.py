"""
File: histogram1.py

Copyright (c) 2016 Rachel Benavente

License: MIT

This code prints out a histogram based upon a list of numbers.
"""

def histogram(number):
    for i in number:
        string = ""
        for h in range(i):
            string += "*"
        print string

histogram ([2,4,6,8])
