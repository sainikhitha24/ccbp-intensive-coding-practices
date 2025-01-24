# The function accepts an array dataSet of m positive integers and an integer m as its arguments.

# You are required to calculate the Standard deviation of m positive integers in the array.


# Let sqrt(y) be square root of a positive integer 'y'.



def calcStandardDeviation(dataSet , m):
    sum = 0
    for i in dataSet:
        sum += i
    average = sum / m 
    standarddeviation = 0 
    for i in dataSet :
        standarddeviation += (i - average)*(i- average)
    a = standarddeviation / m
    return a ** 0.5
m = int(input())
dataSet = list(map(int,input().split()))
result = calcStandardDeviation(dataSet,m)
print(round(result,2))