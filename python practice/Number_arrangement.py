def kindergarten(sentence):
   
    result = [int(i) for i in sentence if i.isdigit()]
    mini = min(result)
    maxi = max(result)
    
    ans = ''
    for i in sentence:
        if i.isdigit():
            if int(i) == mini:
                ans += str(maxi)
            elif int(i) == maxi:
                ans += str(mini)
            else:
                ans += i
        else:
            ans += i
    return ans

if __name__ == "__main__":
    sentence = input()
    result = kindergarten(sentence)
    print(result)
