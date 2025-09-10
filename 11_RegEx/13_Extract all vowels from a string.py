'''
Extract all vowels from a string

Input:

text = "Regular Expressions in Python"


Expected Output:

['e', 'u', 'a', 'E', 'o', 'i', 'o', 'i', 'o']

'''

import re

text = "Regular Expressions in Python"
print(re.findall(r"[aeiouAEIOU]", text))
# ['e', 'u', 'a', 'E', 'o', 'i', 'o', 'i', 'o']
