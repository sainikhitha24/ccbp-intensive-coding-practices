


denominations = [0.1,0.5,1,2,5,10]
total = 0

counts = list(map(int,input().split()))

for i in range(len(counts)):
    total += denominations[i] * counts[i]

print("{:.2f}".format(total))
