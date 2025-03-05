# Project Euler : solution to Problem 1; 
# Marco Busetti;

# For this problem, it is not necessary to use clever math in order to solve, we can just
# brute force our way around it :) 

def main():
	ans = 0
	for i in range(1, 1000):
		if i%5 == 0 or i%3 == 0: ans += i
	print(ans)

if __name__ == '__main__':
	main()
