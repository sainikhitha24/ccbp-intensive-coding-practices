sent = input()
freq = {}
minFreq=float('inf');
maxFreq=float('-inf')
minLetter = ''
maxLetter = ''  

for i in sent :
    if i.isalpha():
        if i in freq:
            freq[i] +=1
        else:
            freq[i] = 1

for key in freq.keys():
    if(minFreq>= freq[key]):
        minLetter = key
        minFreq = freq[key]
    if(maxFreq< freq[key]):
        maxLetter = key
        maxFreq = freq[key]
print(minLetter,maxLetter)
result = ''
for i in sent:
    if i == minLetter:
        result+=maxLetter
    elif i == maxLetter:
        result+=minLetter
    else:
        result+=i
print(result)