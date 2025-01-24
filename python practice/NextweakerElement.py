# You are given an array arr of size n.

# Print the Next Weaker Element (NWE) for every element.

# The Next Weaker Element for an element x is the first element on the right side of x in the array, which is strictly smaller than x.

# If no smaller elements exist to the right of x, consider the next weaker element as -1.

# Input Format:

# The input consists of:

# First line consists n representing the number of elements in the arr.
# Second line consists n space-separated integers representing the elements of arr.
# Output Format:

# Print n space-separated integers representing the next weaker element for each of the elements in arr.


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
