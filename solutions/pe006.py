# Project Euler : solution to Problem 6; 
# Marco Busetti;

# For this problem, we can very easily brute force our way around it.

def main():
	squares = [0, 0]
	for i in range (1, 101):
		squares[0] += i
		squares[1] += i**2
	print(squares[0]**2 - squares[1])

if __name__ == '__main__':
	main()
