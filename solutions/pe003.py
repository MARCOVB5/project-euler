# Project Euler : solution to Problem 3; 
# Marco Busetti;

# For this problem we will just run the prime_factors funcion in eulerlib.py, since 
# we are not dealing with a massive number that needs extra steps/optimizations

import eulerlib as el

def main():
	print(max(el.prime_factors(600851475143)))	

if __name__ == '__main__':
	main()
