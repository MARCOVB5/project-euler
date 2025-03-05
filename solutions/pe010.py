# Project Euler : solution to Problem 10; 
# Marco Busetti;

# This problem is directly solved by using the sieve_of_eratosthenes function in eulerlib.py

import eulerlib as el

def main():
	primes_below_two_million = el.sieve_of_eratosthenes(2*10**6)
	print(sum(primes_below_two_million))	

if __name__ == '__main__':
	main()
