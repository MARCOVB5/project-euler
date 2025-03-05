# Project Euler : solution to Problem 9; 
# Marco Busetti;

# This problem can actually be solved purely algebraically without any code ! 
# The algebraic manipulation is presented below:

'''
We want positive integers a, b and c such that: 
	 a + b + c = 1000  (I)
	 a^2 + b^2 = c^2   (II)
First we can isolate c in equation (I):
	c = 1000 - (a + b) (III)
Thus, substituting in (II) we get:
	a^2 + b^2 = (1000 - (a+b))^2 <=>
	<=> a^2 + b^2 = 1000000 - 2*1000*(a+b) + (a+b)^2 <=>
	<=> a^2 + b^2 = 1000000 - 2000a - 2000b + a^2 + b^2 + 2ab <=>
	<=> 0 = 1000000 - 2000a - 2000b + 2ab <=>
	<=> ab - 1000a - 1000b + 500000 = 0 <=>
	<=> (a - 500)(b - 500) - 250000 = 0 <=>
	<=> (a - 500)(b - 500) = 250000
Finally we solve for a and b taking into consideration that both are positive integers and b > a:
	(a - 500) = 200 
	(b - 500) = 125
Notice that 200 * 125 = 250000
We then get : 
	a = 200
	b = 375
Finally, from (III) : 
	c = 1000  - (200 + 375) = 425
Notice that we have a < b < c
This completes the algebraic manipulation and finding a, b and c.
'''

# From the calculations above, it is only necessary to print the value of 200 * 375 * 425

def main():
	print(200 * 375 * 425)
	
if __name__ == '__main__':
	main()
