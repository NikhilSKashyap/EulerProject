"""
**Problem Statement**\n
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.\n
https://projecteuler.net/problem=21

**Authors**\n
Nikhil S Kashyap

**Language**\n
Python3

**Solution**\n
 First let us write a function to find the factors of a given number
    >>> from math import sqrt
    >>> from functools import reduce
    >>> def factors(n):
    >>>     step = 2 if n%2 else 1
    >>>     return list(set(reduce(list.__iadd__,
    >>>                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if not n % i))))

Now we will write a function to find amicable pairs. 

factors() function will return all the factors but the problem statement says "propoer divisors of n" i.e excluding the number itself. We shall remove it by using pop function and sum the factors.
    >>> factorlist1 = factors(n)
    >>> factorlist1.pop(factorlist1.index(max(factorlist1)))
    >>> factorlistsum1 = sum(factorlist1)

From the example d(220) = 284 and we also check d(284) =220, hence we pass factorlistsum1 to factors() function
    >>> factorlist2 = factors(factorlistsum1)
    >>> factorlist2.pop(factorlist2.index(max(factorlist2)))
    >>> factorlistsum2 = sum(factorlist2)

Now we check if  d(a) = b and d(b) = a and append it to a list
    >>> if n == factorlistsum2 and n!=factorlistsum1:
    >>>     ans.append((n,factorlistsum1))

**Final amicablepair() looks like**\n
    >>> def amicablenumbers(n):
    >>>    ans = []
    >>>    factorlist1 = []
    >>>    factorlist2 = []
    >>>    factorlist1 = factors(n)
    >>>    factorlist1.pop(factorlist1.index(max(factorlist1)))
    >>>    factorlistsum1 = sum(factorlist1)
    >>>    factorlist2 = factors(factorlistsum1)
    >>>    factorlist2.pop(factorlist2.index(max(factorlist2)))
    >>>    factorlistsum2 = sum(factorlist2)
    >>>    if n == factorlistsum2 and n!=factorlistsum1:
    >>>        ans.append((n,factorlistsum1))
    >>>    return ans

**Example**\n
    >>> for i in range(2,10000):
    >>>     ans = amicablenumbers(i)    
    >>>     if len(ans) != 0:
    >>>         print(ans)
    [(220, 284)]
    [(284, 220)]
    [(1184, 1210)]
    [(1210, 1184)]
    [(2620, 2924)]
    [(2924, 2620)]
    [(5020, 5564)]
    [(5564, 5020)]
    [(6232, 6368)]
    [(6368, 6232)]

**Alternate method**\n
Can be solved using sympy package's is_amicable method.\n
https://docs.sympy.org/latest/modules/ntheory.html?highlight=factorint#sympy.ntheory.factor_.is_amicable
"""

from math import sqrt
from functools import reduce

def factors(n):
    """
    Finds factors of any given number n
    """
    step = 2 if n%2 else 1
    return list(set(reduce(list.__iadd__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if not n % i))))

def amicablenumbers(n):
    """
    Checks amicable pair for any given number n and returns empty list if their is no amicable pair.
    """
    ans = []
    factorlist1 = []
    factorlist2 = []
    factorlist1 = factors(n)
    factorlistsum1 = sum(factorlist1.pop(factorlist1.index(max(factorlist1))))
    factorlist2 = factors(factorlistsum1)
    factorlistsum2 = sum(factorlist2.pop(factorlist2.index(max(factorlist2))))
    if n == factorlistsum2 and n!=factorlistsum1:
        ans.append((n,factorlistsum1))
    return ans


if __name__ == '__main__':
    for i in range(2,10000):
        ans = amicablenumbers(i)    
        if len(ans) != 0:
            print(ans)