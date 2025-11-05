# Project Euler : solution to Problem 39; 
# Marco Busetti;

# For the following problem we can simply state that a + b + c = p, thus, 
# c = p - a - b. However, since a² + b² = c², we also know that
# c = sqrt(a² + b²). So we simply check if:
# p-a-b = sqrt(a² + b²) <=> (p-a-b)² = a² + b².

def main():
	n_max = 0 #saves the max num of sols
	p_ans = 1 #saves the related p
	for p in range(1, 1001):
		n_sols = 0 # number of solutions
		for a in range(1, p//2):
			for b in range(1, p//2):
				if a*a + b*b == (p-a-b)*(p-a-b):
					n_sols = n_sols+1
		if n_sols > n_max:
			n_max = n_sols
			p_ans = p
	print(p_ans)

if __name__ == '__main__':
	main()
