# Zachery Gentry

import csv
import numpy as np
from numpy import linalg as la



f = open('data-communications.csv', 'rt')

reader = csv.reader(f)

# Original uncorrupted bits.
# Is each set of 10 data points closer to pulse0 or pulse1?
pulse0 = np.ones(10)
pulse0 = pulse0/np.linalg.norm(pulse0)
pulse1 = np.append(np.ones(5), -1*np.ones(5))
pulse1 = pulse1/np.linalg.norm(pulse1)

pulseNorm = la.norm(pulse0)

# Only 1 row, runs one time
for row in reader:
    row = np.array(row)
    # Split row into arrays of length 10
    numbers = np.array(np.split(row, len(row) / 10)).astype(np.float)

def getBit(dot0, dot1, normProduct):
    val1 = abs(normProduct - dot0)
    val2 = abs(normProduct - dot1)
    if(val1 < val2):
        return '0'
    else:
        return '1'

bits = []
for value in numbers:
    dot0 = abs(np.dot(value, pulse0))
    dot1 = abs(np.dot(value, pulse1))

    valueNorm = la.norm(value)
    normProduct  = valueNorm * pulseNorm

    bit = getBit(dot0, dot1, normProduct)
    bits.append(bit)

bits = np.array(bits)

bitSets = np.array(np.split(bits, len(bits) / 8))
s = ""
for bitSet in bitSets:
    binary = ''.join(bitSet)
    binary_int = int(binary, 2)
    character = chr(binary_int)
    s = s + character

print(s)