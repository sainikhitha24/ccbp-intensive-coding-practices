def min_xor_flips(A, B, Z):
    current_xor = A ^ B
    flips = bin(current_xor ^ Z).count('1')
    return flips

A = int(input())
B = int(input())
Z= int(input())
print(min_xor_flips(A, B, Z))
