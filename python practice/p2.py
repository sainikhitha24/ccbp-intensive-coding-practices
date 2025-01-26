n = input("Enter a number: ")
name_length = len(n)
first = []
second = []
for i in range(0, name_length):
    if i % 2 == 0:
        first.append(n[i])
    else:
        second.append(n[i])
print(" ".join(first))
print(" ".join(second))