# The MEX Number of a non-negative set of numbers is the smallest non-negative number that is not present in the set. For example, MEX({2, 4, 11}) = 0, and MEX({0, 2, 3, 9}) = 1.

# Your task is to take a given array A of length l and remove the minimum number of elements from it so that the MEX value of the modified array is not equal to the MEX value of the original array.   

# Your code should print the minimum number of elements that need to be removed from the array.
# If the task is not possible, then your code should print -2   
# Input

# First line contains an integer l, representing the size of the array A.
# Second line contains elements of the array A, separated by space.
# Output

# The output consists of an integer.


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