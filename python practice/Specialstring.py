
# **Special String**

# Teja has a list of words, and he considers a word as special if it has the maximum number of distinct letters among all the words. 

# If there is more than one such word, the word that comes first in alphabetical order is special.

# Write a program to help Teja find the special word.

# **Note:** Consider upper and lower case letters are different.

# **Input**

# The input is a string that contains the words separated by a space.

# **Output**

# The output is a string that represents the special word as mentioned above.


words = input().split()
words.sort()
more_char_word = words[0]
char_count = len(set(words[0]))
for w in words:
    w_char_count = len(set(w))
    if w_char_count > char_count:
        more_char_word = w
        char_count = w_char_count
print(more_char_word)
