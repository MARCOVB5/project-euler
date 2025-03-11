# Project Euler : solution to Problem 17; 
# Marco Busetti;

# For this problem we can simply use the famous "num2words" library in Python !

from num2words import num2words

def main():
	ans = 0
	for i in range(1, 1001):
		num_word = num2words(i)
		for j in range(len(num_word)):
			if num_word[j] != '-' and num_word[j] != ' ':
				ans += 1
	print(ans)

if __name__ == '__main__':
	main()
