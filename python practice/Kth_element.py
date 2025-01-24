element = int(input())
listlength = list(map(int,input().split()))
k = int(input())
sum = 0
if k > len(listlength):
    print(0)
else:
   
    for i in range(element):
        if (i+1) % k == 0:
            sum += listlength[i]

    print(sum)