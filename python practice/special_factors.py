# Ram was given an assignment by his teacher to find the special factors of a positive number N.

# A factor is a number which exactly divides the given number (including the number). A factor is special if it is a prime number.

# Help Ram by identifying all the special factors of the number N.

# Write a program that reads the number N and prints the special factors of the number N.

# input

# The input will be a single line containing an integer representing a positive number N.

# Output

# The output should be a single line containing the space-separated special factors of the number N in ascending order.

# Explanation

# Test Case: If N = 20

# The factors of 20 are 1, 2, 4, 5, 10, 20. Whereas the special factors are 2, 5.

# The output should be 2 5

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True        
def findprime(arr):
    return [str(num) for num in arr if isPrime(num)]

N = int(input())
arr = []
for i in range(1,N+1):
    if N % i == 0 :
        arr += [i]
prime = findprime(arr)
print(" ".join(prime))