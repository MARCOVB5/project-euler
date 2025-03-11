# Project Euler : solution to Problem 14; 
# Marco Busetti;

# We will be using memoization in order to optimize this problem. 
# The main idea is to save previous already calculated chains of a given 
# Collatz Sequence in order to avoid re-calculations of the same results of a chain.  

def collatz_length(n, cache):
    """
    Funtion that returns the length of the Collatz chain starting at n, using memoization.
    - Parameters: integer n (starting number) and cache (dictionary)
    - Time Complexity: O(log(n)) (empirically)
    """
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        length = 1 + collatz_length(n // 2, cache)
    else:
        length = 1 + collatz_length(3 * n + 1, cache)
    cache[n] = length
    return length

def main():
    max_len = 0
    ans = 0
    cache = {}

    for i in range(1, 10**6):
        c_len = collatz_length(i, cache)
        if c_len > max_len:
            max_len = c_len
            ans = i
    
    print(ans)

if __name__ == '__main__':
	main()
