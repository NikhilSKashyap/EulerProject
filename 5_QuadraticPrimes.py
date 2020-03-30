"""
**Problem Statement**\n

Euler discovered the remarkable quadratic formula 
:math:`n^2+n+41` \n
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when ``n=40,402+40+41=40(40+1)+41`` is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
The incredible formula :math:`n^2−79n+1601` was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.\n
Considering quadratics of the form:\n
:math:`n^2+an+b`, where :math:`|a|<1000` and :math:`|b|≤1000`\n
where :math:`|n|` is the modulus/absolute value of n \n
e.g. :math:`|11|=11` and :math:`|−4|=4` \n
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.\n
https://projecteuler.net/problem=27  

**Authors**\n
Nikhil S Kashyap

**Language**\n
Python3

**Solution**\n
The solution is taken from https://radiusofcircle.blogspot.com/2016/04/problem-27-project-euler-solution-with-python.html
"""
import time


def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

def is_prime(n):
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

primes1000 = sieve(1000)

primes = primes1000[:]

largest = 0

for b in primes1000:
	for a in primes1000:
		i = 0
		while True:
			quadratic = i**2+a*i+b
			if quadratic not in primes:
				if is_prime(quadratic):
					primes.append(quadratic)
				else:
					if i-1 > largest:
						largest = i-1
						axb = a*b
					break
			i += 1
		i = 0
		while True:
			quadratic = i**2-a*i+b
			if quadratic not in primes:
				if is_prime(quadratic) and quadratic>0:
					primes.append(quadratic)
				else:
					if i-1 > largest:
						largest = i-1
						axb = -1*a*b
					break
			i += 1

print(sieve(10))
print(axb)
