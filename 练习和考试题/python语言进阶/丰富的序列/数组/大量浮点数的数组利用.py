from array import array
from random import random

float = array('d', (random() for i in range(10 ** 7)))
fp = open('floats.bin', 'wb')
float.tofile(fp)
fp.close()
print(float[-1])

float2 = array('d')
fp = open('floats.bin', 'rb')
float2.fromfile(fp, 10 ** 7)
fp.close()
print(float2[-1])
