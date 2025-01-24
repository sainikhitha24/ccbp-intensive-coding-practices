n = int(input())
lis = []
for i in range(n):
    a = int(input())
    lis.append(a)

leng = len(lis)
diff=0
sum=0
if(leng> 2):
    for index, number in enumerate(lis):
        if(index %2==0):
            sum+=number
        else:
            diff+=number
else:
    print("Invalid")

print(abs(sum-diff))