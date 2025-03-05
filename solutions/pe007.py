# Project Euler : solution to Problem 7; 
# Marco Busetti;

# For this problem, we can brute force our way around it by checking if each number is prime or not. 

import eulerlib as el

def main():
	temp = 0
	ans = 2
	while temp < 10001:
		if el.is_prime(ans): temp += 1	
		ans += 1
	print(ans - 1)

if __name__ == '__main__':
	main()
