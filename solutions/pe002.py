# Project Euler : solution to Problem 2; 
# Marco Busetti;

# For this problem we will be using Binet's Formula in order to calculate
# the n-th number of the Fibonacci Sequence.
# This significantly improves the time necessary to solve the problem.
# In this case, we notice our time complexity is O(nlog(n))

import eulerlib as el

def main():
	ans = 0
	i = 0
	fib = el.fibonacci(i)
	while (fib <= 4000000):
		if (fib % 2 == 0): ans += fib
		i += 1;
		fib = el.fibonacci(i);
	print(ans)

if __name__ == '__main__':
	main();
