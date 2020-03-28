"""
**Problem Statement**\n
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.\n
https://projecteuler.net/problem=1

**Authors**\n
Nikhil S Kashyap

**Language**\n
Python3
"""


class SumofListofMultiples():
    '''
    Finds sum of multiples of 3 and 5 under any given number n

    **Code:**\n
    >>> def sumoflistofmultiples(n):
    >>>    multiplesofthree = list(range(3, (n + 1), 3))
    >>>    sum_multiplesofthree = sum(multiplesofthree)
    >>>    multiplesoffive = list(range(5, (n + 1), 5))
    >>>    sum_multiplesoffive = sum(multiplesoffive)
    >>>    return sum_multiplesoffive + sum_multiplesofthree

    **range()** takes three parameters - Starting element, Last element and the Interval.
    For example ``list(range(0,4,1))`` prints ``[0,1,2,3]`` and ``list(range(0,4,2))`` prints ``[0,2]``

    **sum()** adds all the elements in the list

    **Alternate Code:**\n
    >>> def sumoflistofmultiples(n):
    >>>     return sum(list(range(3,(n+1),3))) + sum(list(range(5,(n+1),5)))
    '''

    def __init__(self):
        self.multiplesofthree = []
        self.multiplesoffive = []

    def sumoflistofmultiples(self, n):
        '''
        **Parameters:**\n
        n : Integer
            Last element

        **Variables:**\n
        multiplesofthree: List
                            List of multiples of 3 under given number n
        multiplesoffive: List
                            List of multiples of 5 under given number n

        **Example:**\n
        >>> sumoflistofmultiples = SumofListofMultiples()
        >>> sum = sumoflistofmultiples.sumoflistofmultiples(1000)
        >>> print(sum)
        >>> 267333
        '''
        self.multiplesofthree = list(range(3, (n + 1), 3))
        sum_multiplesofthree = sum(self.multiplesofthree)
        self.multiplesoffive = list(range(5, (n + 1), 5))
        sum_multiplesoffive = sum(self.multiplesoffive)
        return sum_multiplesoffive + sum_multiplesofthree


if __name__ == "__main__":
    sumoflistofmultiples = SumofListofMultiples()
    sum = sumoflistofmultiples.sumoflistofmultiples(1000)
    print(sum)
