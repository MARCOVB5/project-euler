# Project Euler : solution to Problem 29; 
# Marco Busetti;

# The solution can be easily found by using the 'set' data structure.

def main():
	s = set()
	for i in range(2, 101):
		for j in range(2, 101):
			s.add(i**j)
	print(len(s))

if __name__ == '__main__':
	main()
