# Project Euler : solution to Problem 99; 
# Marco Busetti;

# The idea of this problem will be using logarithms to have the job done. 
# Since the logarithms we are dealing with are strict crescent functions, 
# for every positive real numbers a and b such that a < b, we have: log(a) < log(b). 

import math as mt

def main():

	max_value = 1
	i = 1 # starts at line 1	

	with open('0099_base_exp.txt', 'r') as f:
		for line in f:
			base_str, exp_str = line.strip().split(',')
			base = int(base_str)
			exp = int(exp_str)
			if exp*mt.log(base) > max_value: 
				max_value = exp*mt.log(base)
				ans = i
			i += 1  
	
	print(ans)
	

if __name__ == '__main__':
	main()
