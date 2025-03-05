# Project Euler : solution to Problem 4; 
# Marco Busetti;

# We can solve it through brute force :)

import eulerlib as el

def main():
	max_palindrome = 1 
	for i in range(100, 1001):
		for j in range(100, 1001):
			if el.is_palindrome(i*j) and i*j > max_palindrome:
				max_palindrome = i*j
	print(max_palindrome)	

if __name__ == '__main__':
	main()
