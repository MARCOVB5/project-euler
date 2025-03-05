# Project Euler : solution to Problem 20; 
# Marco Busetti;

# We can just solve it directly by brute force.

import math as mt

def main():
	n = mt.factorial(100)
	ans = 0
	while n > 0:
		ans += n%10
		n //= 10
	print(ans)	

if __name__ == '__main__':
	main()
