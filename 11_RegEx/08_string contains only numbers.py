'''
Find all 4-digit years in a text.
Input: "World War happened in 1945, Independence in 1947"
Output: ['1945', '1947']

'''
import re

s1 = "12345"
s2 = "12a45"

print(bool(re.fullmatch(r"\d+", s1)))  # True
print(bool(re.fullmatch(r"\d+", s2)))  # False
