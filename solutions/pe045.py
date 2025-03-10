# Project Euler : solution to Problem 45; 
# Marco Busetti;

# Notice how every Hexagonal Number is also Triangle:
# T_{2n-1} = H_n for all natural n.

# We can simplify the problem that way by only checking which hexagonal numbers are equal to pentagonal numbers.

def main():
	check = 0
	n = 2
	m = 2
	while check < 2 :
		hexa = n*(2*n - 1)
		penta = m*(3*m - 1)/2
		if hexa == penta: 
			check += 1
			n += 1
		elif hexa > penta: m += 1
		else: n += 1
	print(hexa)

if __name__ == '__main__':
	main()
