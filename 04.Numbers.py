from cgi import print_directory
from math import *
# MATH MODULE allows us to do alot of math function

# Basic Arithmetic
print( 3 + 2 ) #  - , *, /, %
print(3 * (4 + 5))

my_num = 5
print(my_num)
# converting number in strings
print(str(my_num) + "my favourite number")

# TypeError -- Unsupported operand type 
# Python do not concatinate strings with numbers
#print(my_num + "my favourite number") 

# MATHS FUNCTION IN PYTHON

my_num = -5 
# ABSOLUTE FUNCTION
# To print the absolute number
print(abs(my_num)) 

# POWER FUNCTION
print(pow(2, 3))

# MAXIMUM -- to print the maximum of the given number
print(max(4, 6))

# MINIMUM  -- to print the minimum of the given number
print(min(4, 6))

# ROUND FUNCTION
print(round(4.9)) # o/p - 5

# Functions which can be acces using math library

# FLOOR
# Rounds a number down to the nearest integer
print(floor(10.76))

# CEIL
# Rounds a number up to the nearest integer
print(ceil(10.45))

# SQRT
# Returns the square root of the number
print(sqrt(36))
