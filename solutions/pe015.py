# Project Euler : solution to Problem 15; 
# Marco Busetti;

# For this problem it is sufficient to do a combinatoric analysis as it follows : 

'''
Notice that, in order to reach the destination, we have to move right and down exactly 20 times each.
That gives us the total number of moves of 40. 
Let R = go right and D = go down. 
Each valid path is just an arrangement of the letters "R...D" (Right, ..., Down). 
The number of unique ways to arrange these moves is:
Total Ways = Ways to arrange (R, ..., D)
Since we have 20 R and 20 D, we have the following formula derived from the binomial coefficient: 
Ways = 40! / (20! * 20!)
'''

# Thus we only need to compute the numeric value above.

from math import factorial

def main():
	print(int(factorial(40)/(factorial(20)*factorial(20))))

if __name__ == '__main__':
	main()
