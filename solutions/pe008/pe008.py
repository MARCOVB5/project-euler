# Project Euler : solution to Problem 8; 
# Marco Busetti;

# Since we are dealing with an array with a lenght of only 1000 items, we can simply brute force our way 
# around it :)
# In order to achieve a cleaner code, the large number is pasted on a separated .txt file and imported.
# Then we save it in an array, where each case it's one digit of the original number.

with open('large_number.txt', 'r') as f:
	data = f.read()

def main():
	max_product = -1
	large_number = [int(ch) for ch in data if ch.isdigit()]
	for i in range(len(large_number) - 13):
		temp_product = 1
		for j in range(13):
			temp_product *= large_number[i + j]
		if (temp_product > max_product): max_product = temp_product
	print(max_product)

if __name__ == '__main__':
	main()
