# Andy wants to play a game with you. He has given you a positive integer N greater than 2, and you need to tell him the two prime numbers whose sum is equal to N. There might be several combinations possible such type. To win the game, you need to find the pair whose minimum value is the smallest among all the minimum values of pairs.

# If there are no such pairs found, print -1

# Input

# The input is a single line containing a positive integer N.

# Output

# The output should be a single line containing two space-separated integers in ascending order, whose sum is equal to N.

# Explanation

# In the example, the given number is 74.

# The possible combinations are (3, 71) and (71, 3).

# Where the smallest value among the above two pairs is 3.

# The pair whose minimum value is smallest among the above two pairs is (3, 71)

# So, the output should be 3 71


def check_i_is_prime_number(num):
    if num < 2:
        return False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num%i == 0:
            return False
    
    return True

def prime_divison(N):
    for i in range(2, N):
        is_i_prime = check_i_is_prime_number(i)
        if is_i_prime:
            j = N-i
            is_j_prime = check_i_is_prime_number(j)
            if is_j_prime and is_j_prime:
                print(i, j)
                return 
    print("-1")

N = int(input())
prime_divison(N)
        