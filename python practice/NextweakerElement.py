def NextweakerElement(N, array):
    result = []
    for i in range(N):
        found = False
        for j in range(i + 1, N):
            if array[j] < array[i]:
                result.append(array[j])
                found = True
                break
        if not found:
            result.append(-1)  
    return result


N = int(input())
array = list(map(int, input().split()))

result = NextweakerElement(N, array)
print(" ".join(map(str, result)))
