# Project Euler : solution to Problem 56; 
# Marco Busetti;

# This problem can be solved by pure brute force ! 

def digit_sum(n):
	'''
	Returns the digital sum of a given integer n 
	- Parameters: an integer n
	- Returns: the digital sum of an integer n
	- Time complexity: O(log(n))
	'''
	ds = 0
	while n > 0: 
		ds += n%10
		n //= 10
	return ds	
				
def main():
	ans = -1
	for a in range(1, 101):
		for b in range(1, 101):
			if digit_sum(a**b) > ans: ans = digit_sum(a**b)
	print(ans)	

if __name__ == '__main__':
	main()
