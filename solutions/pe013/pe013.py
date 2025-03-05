# Project Euler : solution to Problem 13; 
# Marco Busetti;

# As in problem 008, we will write in a separate file the large number (actually numbers !). 
# Then we can solve it by simply using brute force :)

import math as mt

numbers = []
with open('large_number.txt', 'r') as f:
	numbers = [int(line.strip()) for line in f if int(line.strip())]

def main():
	ans = 0
	for i in range(100):
		ans += numbers[i]
	ans = int(str(ans)[:10])
	print(ans)

if __name__ == '__main__':
	main()
