'''
Check if a string starts with "Hello".
Input: "Hello World" → Output: True
Input: "World Hello" → Output: False

'''

import re

text1 = "Hello World"
text2 = "World Hello"

print(bool(re.match(r"^Hello", text1)))  # True
print(bool(re.match(r"^Hello", text2)))  # False
