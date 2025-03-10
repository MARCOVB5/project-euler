# Project Euler : solution to Problem 41; 
# Marco Busetti;

# In order to simplify the necessary iterations, we can simply check if the number is divisible by 3. 
# Notice that a number is divisible by when the sum of its digits is also divisible by 3. 
# If a given number is divisible by 3, it is not a prime number. 
# For the pandigital numbers case we can notice quite simply that only 4 and 7 digit numbers can be prime 
# and pandigital at the same time --> We check if n(n+1)/2 is a multiple of 3 or not !  
# Thus we can iterate only in those intervals :D

# We'll be using the functions is_pandigital and is_prime defined in eulerlib.py ! 

import eulerlib as el

def main():
	ans = -1
	for i in range(1000, 10000):
		if el.is_prime(i) and el.is_pandigital(i) and i > ans:
			ans = i
	for i in range(10**6, 10**7):
		if el.is_prime(i) and el.is_pandigital(i) and i > ans:
			ans = i
	print(ans)
	

if __name__ == '__main__':
	main()
