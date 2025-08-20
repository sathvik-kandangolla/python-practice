''' Count the frequency of each character in a string

Input: "banana"
Expected Output: {'b':1, 'a':3, 'n':2}'''

from collections import Counter

def char_frequency(s):
    return dict(Counter(s))

print(char_frequency("banana"))

