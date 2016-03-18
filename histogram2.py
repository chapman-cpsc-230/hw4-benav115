"""
File: histogram2.py

Copyright (c) 2016 Rachel Benavente

License: MIT

This code prints out a histogram based upon a list of numbers in a fancy format.
"""

def histogram(number):
    print """
     n  | Data
    ---+------------------
    """
    for i in number:
        string = ""
        for h in range(i):
            string += "*"
        print """
        %d | %s
        """ % (i, string)

histogram ([2,4,6,8])
