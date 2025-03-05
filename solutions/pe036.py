# Project Euler : solution to Problem 36; 
# Marco Busetti;

# We can solve this problem directly by using the is_palindrome function defined in eulerlib.

import eulerlib as el

def main():
	ans = 0
	for i in range(1, 10**6):
		if el.is_palindrome(i) and el.is_palindrome(int(bin(i)[2:])): ans += i
	print(ans)

if __name__ == '__main__':
	main()
