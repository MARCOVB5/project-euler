# Project Euler : solution to Problem 19; 
# Marco Busetti;

# This problem could be solved by logic alone, however, let's present here 
# a very straightforward  way of solving the problem. 

def main():
    ans = 0
    year = 1900
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_week = 0  # 0 = Monday for Jan 1, 1900
    
    while year < 2001:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            months[1] = 29
        else:
            months[1] = 28
        
        month = 0
        while month < len(months):
            if day_of_week == 6 and year >= 1901:
                ans += 1
            
            day_of_week = (day_of_week + months[month]) % 7
            month += 1
        
        year += 1
    
    print(ans)

if __name__ == '__main__':
    main()

