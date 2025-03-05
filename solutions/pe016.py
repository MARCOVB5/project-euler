# Project Euler : solution to Problem 16; 
# Marco Busetti;

# For this problem we can just solve it directly as it follows.

def main():
	n = 2**1000
	ans = 0
	while n > 0:
		ans += n%10
		n //= 10
	print(ans)

if __name__ == '__main__':
	main()
