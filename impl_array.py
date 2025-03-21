# Implementing array in python
from array import *

# Only homogeneous elements are allowed in array
# i -> integer
# f -> float
# d -> double
# c -> character
# b -> byte
# u -> unicode character
# h -> short integer
# H -> unsigned short integer
# l -> long integer 
# L -> unsigned long integer
# q -> long long integer
# Q -> unsigned long long integer
# f -> float
# d -> double   
# b -> boolean
# array(typecode, [initializers])

arr = array('i', [1, 2, 3, 4, 5])
for i in arr:
    print(i)



