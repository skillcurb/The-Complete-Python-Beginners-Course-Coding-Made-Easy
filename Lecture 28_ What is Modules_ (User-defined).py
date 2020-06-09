import my_module

# We can use dir() to find names that are defined inside a module
dir(my_module)

my_module.greeting('Samantha')

my_module.add(1,2,3)

# aliasing or renaming a module
import num_module as nm

dir(nm)

nm.square(2)

nm.tbl(3)

from my_module2 import func1

func1

func1()

# Built-in Modules

# Mathematical Module
import math as m

# Value of PI
m.pi

# Euler's number and it is a base of the natural logarithm. 
m.e

m.radians(30)

# trignometric ratios for the angle of 30 degrees (0.5235987755982988 radians)
m.sin(5235987755982988)

m.cos(5235987755982988)

m.tan(5235987755982988)

m.exp(10)

m.sqrt(25)

m.ceil(8.5897)

m.floor(8.5897)

import sys

sys.path

# Displays python interpreter current version
sys.version

# Python - OS Module
import os

# create a new directory using the mkdir() function from the OS module
os.mkdir("d:\\demodir")

# import statstical module
import statistics as st

st.mean([2,1,5,9])

st.median([2,1,5,9])

st.mode([2,2,1,5,9,2])

st.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5])

#Data Compression and Archiving
import zipfile

for filename in [ 'nb1.csv', 'example.zip','ex2.zip', 'notthere.zip' ]:
    
    print(filename, zipfile.is_zipfile(filename))