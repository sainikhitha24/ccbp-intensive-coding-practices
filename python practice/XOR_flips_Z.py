
# Minimum XOR Flips for Z

# You are given three integers A, B, and Z. Your task is to convert these numbers into binary representation and find out the least number of bits that need to be flipped in A and B such that the XOR operation between A and B results in Z.

# Input:

# The input consists of three lines:

# The first line contains the integer A.
# The second line contains the integer B.
# The third line contains the integer Z.
# Output:

# Output a single integer which represents the minimum number of bits that need to be flipped to satisfy the condition.

# Sample Input 1

# 1
# 2
# 3

# Sample Output 1

# 0


def min_xor_flips(A, B, Z):
    current_xor = A ^ B
    flips = bin(current_xor ^ Z).count('1')
    return flips

A = int(input())
B = int(input())
Z= int(input())
print(min_xor_flips(A, B, Z))
