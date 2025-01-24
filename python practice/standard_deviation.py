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