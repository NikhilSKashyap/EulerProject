"""
**Problem Statement**\n
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?\n
https://projecteuler.net/problem=15

**Authors**\n
Nikhil S Kashyap

**Language**\n
Python3

**Solution**\n
It is a simple Combination problem and the formula is ``(N+N)!/N!*N!``

**Code**\n
**To find the factorial of N**\n
>>> def factorial(N): 
>>> 	result = 1
>>> 	while (N > 0): 	
>>>         result = result * N 
>>>         N -= 1	
>>> 	return result

**To find the value of Numerator**\n
>>> factorial(N+N)

**To find the value of Denominator**\n
>>> factorial(N)*factorial(N)
"""

def factorial(N):
    """
    Calculates the factorial of any given number N
    """
    result = 1
    while (N > 0):
        result = result * N
        N -= 1
    return result

def latticepaths(N): 
    """
    Finds the number of routes from top-left corner of any given grid N*N to bottom-right corner.
    """
    numerator = factorial(N + N) 
    denominator = factorial(N)*factorial(N)
    return int(numerator/denominator) 

if __name__ == "__main__" : 
	print(latticepaths(20))

