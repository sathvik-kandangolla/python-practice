'''
Find duplicate words in a sentence.
Input: "This is is a test test line"
Output: ['is', 'test']

'''


import re 

text = "This is is a test test line"
print(re.findall(r"\b(\w+)\s+\1\b", text))
# ['is', 'test']
