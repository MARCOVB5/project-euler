# Project Euler : solution to Problem 5; 
# Marco Busetti;

# The problem is easily solved if we apply the following formula from Number Theory:
# a * b = lcm(a, b) * gcd(a, b), where a and b are two positive integers

import eulerlib as el

def main():
	ans = 1
	for i in range (2, 21):
		ans = el.lcm(ans, i)
	print(ans)	
	
if __name__ == '__main__':
	main()
