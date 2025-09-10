'''
Find all words starting with a capital letter.
Input: "Python is Great and Fun"
Output: ['Python', 'Great', 'Fun']

'''
import re

text = "Python is Great and Fun"
print(re.findall(r"\b[A-Z][a-zA-Z]*\b", text))
# ['Python', 'Great', 'Fun']
