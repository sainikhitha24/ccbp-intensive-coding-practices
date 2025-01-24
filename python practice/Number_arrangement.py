
# Each student from the kindergarten was given a word or a number. Initially the students are standing in the given order of input. Later the students that have numbers are told to shuffle among themselves such that they appear in decreasing order when the whole sentence is read. Find the sentence formed after they rearranged themselves in the said order. 1    
#  1.

# Implement your logic in the function kindergarten provided.

# Input Format:

# The input is a string containing the actual sentence.
# The numbers in the sentence are integers and the numbers are >= 0
# Output Format:

# Return a string containing the modified sentence as mentioned above



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
