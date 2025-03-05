# A useful library for solving Project Euler problems; 
# Marco Busetti;

import math as mt

def lcm(a, b):
	'''
	Function that returns lcm of 2 numbers based on 
	the formula : a * b = lcm(a, b) * gcd(a, b),
	where a and b are 2 integers. 
	- Parameters: integers a and b
	- Returns: lcm of a and b
	- Time complexity: O(log(min(a,b))) 
	'''
	return (a * b) // mt.gcd(a, b)


def fibonacci(n):
	'''
	Function that returns the n-th number of Fibonacci.
	Also called as Binet's Formula.
	- Parameters : integer n
	- Returns : n-th number of Fibonacci Sequence (F(n))
	- Time complexity : O(log(n))
	'''
	phi = (1 + mt.sqrt(5)) / 2
	psi = (1 - mt.sqrt(5)) / 2
	return round((phi**n - psi**n) / mt.sqrt(5))


def prime_factors(n):
	'''
	Function that returns the prime factors of a given integer n.
	- Parameters : integer n
	- Returns : an array containing the prime factors of n
	- Time complexity : O(sqrt(n))
	'''
	factors = []
   	 
	#excludes multiples of 2
	while n % 2 == 0: 
		factors.append(2)
		n //= 2

	#checks the odd numbers until sqrt(n)
	i = 3 
	while i * i <= n: 
		while n % i == 0:
			factors.append(i)
			n //= i
		i += 2

	#if there's a prime number greater than sqrt(n)
	if n > 1: 
		factors.append(n)

	return factors

def sieve_of_eratosthenes(n):
	'''
	Function that marks which numbers are prime until positive integer n.
	Parameters: positive integer n
	Returns: an array of all prime numbers up to n
	Time complexity: O(nlog(log(n)))
	'''
	if n < 2 : return []
	sieve = [True] * (n+1) # Boolean list to mark prime numbers
	sieve[0], sieve[1] = False, False # Numbers 0 and 1
	limit = int(mt.sqrt(n))

	for i in range(2, limit + 1):
		if sieve[i]: # If integer i is prime 
			for j in range(i * i, n + 1, i): sieve[j] = False

	primes = [i for i, is_prime in enumerate(sieve) if is_prime]

	return primes


def is_prime(n):
	'''
	Function that returns 1 if a positive integer n is prime 
	and 0 if not.
	- Parameters: integer n
	- Returns: 1 if n is prime and 0 if not
	- Time complexity: O(sqrt(n))
	'''
	if n < 2: return 0 
	if n in (2,3): return 1
	if n % 2 == 0 or n % 3 == 0: return 0
	limit = int(mt.sqrt(n))
	for i in range(5, limit + 1, 6):
		if n % i == 0 or n % (i+2) == 0 : return 0
	return 1 


def is_palindrome(n):
	'''
	Returns 1 if n is a palindrome and 0 if not.
	- Parameters: integer n
	- Returns: 1 if n is a palindrome and 0 if not
	- Time complexity: O(log(n))
	'''
	original = n
	reversed_num = 0

	while n > 0:
		reversed_num = reversed_num * 10 + n % 10
		n //= 10

	return original == reversed_num	


