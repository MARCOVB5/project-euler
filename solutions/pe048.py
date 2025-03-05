# Project Euler : solution to Problem 48; 
# Marco Busetti;

# For the following problem it is not necessary to do any complicated simplification;
# We can just brute force our way around it. 

def main():
	ans = 0
	for i in range(1, 1001):
		ans += i**i
	print(ans % (10**10))

if __name__ == '__main__':
	main()
