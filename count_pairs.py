"""
File: count_pairs.py

Copyright (c) 2016 Rachel Benavente

License: MIT

This code counts how many times the string "AT" appears in a DNA string.
"""

def count_v2(dna,base):
    i = 0
    for AT in dna:
        if AT == base:
            i += 1
    return dna.count(base)

dna = 'CAGGCACTTGATAT'
base= "AT"
n = count_v2(dna,base)
print '%s appears %d times in %s' % (base,n, dna)
