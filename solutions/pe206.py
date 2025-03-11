# Project Euler : solution to Problem 206; 
# Marco Busetti;

# We will take a brute force approach for Problem 206. 
# Notice that we have limited the inferior limit and the superior limit to 
# 10**9 and 2*10**9 respectively. 
# Those boundaries are easily deduced from the format / number of digits of the original number 
# in the problem. 

def main():
	for n in range(10**9, 2*10**9, 10):
		n_sqrt = (n**2)//100
		j = 9
		while n_sqrt > 0: 
			if n_sqrt%10 == j: 
				n_sqrt //= 100
				j -= 1				
			else: break 
		if n_sqrt <= 0:
			print(n)
			break

if __name__ == '__main__':
	main()
