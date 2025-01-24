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