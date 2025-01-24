I = int(input())  
arr = list(map(int, input().split()))  


unique_elements = set(arr)
mex = 0
while mex in unique_elements:
    mex += 1

min_element = min(unique_elements)
arr.remove(min_element)

unique_elements_after_removal = set(arr)
mex_after_removal = 0
while mex_after_removal in unique_elements_after_removal:
    mex_after_removal += 1

if mex != mex_after_removal:
    print("1")
else:
    print("-2")