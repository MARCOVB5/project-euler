# Project Euler : solution to Problem 25; 
# Marco Busetti;

# For counting the digits for the n-th Fibonacci number we can simply use the logarithm method :)
# Note that, for big values of n, Binet's Formula for calculating the n-th Fibonacci number can be 
# simplified. That is: 

'''
	n --> infinity => psi^n --> 0
	Thus F_n ~ phi^n / sqrt(5) 
'''

import math as mt

def main():
	phi = (1 + mt.sqrt(5))/2
	n = 1
	digits = 1
	while digits < 1000:
		n += 1
		digits = int(n*mt.log10(phi) - mt.log10(5) / 2) + 1 
	print(n)
		

if __name__ == '__main__':
	main()
