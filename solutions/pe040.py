# Project Euler : solution to Problem 40; 
# Marco Busetti;

# We can solve Problem 40 without any code at all.
# We can simply develop the logic behind the number and arrive at the answer. 
# However, it is presented here a way of solving it by brute force by generating the number as a string. 
# It has a simple implementation in Python and it consumes a moderate ammount of memory.

def main():
	num = "0" + "".join(str(i) for i in range(1, 1000001))
	print(int(num[1])*int(num[10])*int(num[100])*int(num[1000])*int(num[10000])*int(num[100000])*int(num[1000000]))	

if __name__ == '__main__':
	main()
