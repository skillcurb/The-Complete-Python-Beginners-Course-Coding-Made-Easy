#using built-in module
import math as m

print(m.pi)

print(m.e)

print(m.hypot(3,2))

print(m.pow(2,3)) 

print(m.sqrt(4))

val = 3.678
print(m.ceil(val))
print(m.floor(val))

print(m.log(1))

print(m.exp(1))

# trigonometric functions
print(m.radians(30))

print(m.degrees(0.52))

print(m.degrees(m.sin(0.5235)))

print(m.degrees(m.cos(0.5235)))

print(m.degrees(m.tan(0.5235)))

print(m.degrees(m.asin(0.5235)))

m.sinh(m.pi)

import sys

print(sys.path)

sys.version

import os

os.mkdir("d:\\demo")

# import statistical  module
import statistics as st

print(st.mean([2,3,5,10]))

print(st.median([2,3,5,10]))

print(st.mode([2,3,2,2,5,10]))

print(st.stdev([2,3,2,2,5,10]))

print(st.variance([2,3,2,2,5,10]))

#Data Compression and Archiving
import zipfile

for file in ['nb1.csv','example.zip','ex2.zip','not.zip']:
    print(file,zipfile.is_zipfile(file))