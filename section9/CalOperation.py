# Approach1:

import Calculator

print(Calculator.add(10,2))
print(Calculator.subtract(10,5))

# Approach2:

from Calculator import add,mul

print(add(8,2))
print(mul(10,5))

# Approach2:

from Calculator import *

print(add(5,2))
print(subtract(6,3))
print(mul(5,3))

