# Project Euler : solution to Problem 12; 
# Marco Busetti;

# We can brute force our way around this problem :) 

import math as mt

def triangular(n):
	'''
	Returns the n-th triangular number.
	- Parameters: integer n
	- Returns: n(n+1)/2 -> n-th triangular number
	- Time complexity: O(1)
	'''
	return n*(n+1)/2
		
def divisors(n):
	'''
	Returns the number of divisors of an integer n.
	- Parameters: integer n
	- Returns: an integer d of divisors of n 
	- Time complexity: O(sqrt(n))
	'''
	d = 0
	for i in range(1, int(mt.sqrt(n)) + 1):
		if n % i == 0: 
			if i * i == n: d+=1
			else: d+=2	
	return d
	
def main():
	n = 1 
	div = 0 
	while div < 500:
		tri = triangular(n)
		div = divisors(tri)
		n += 1 
	print(int(tri))	
	

if __name__ == '__main__':
	main()
