'''
Extract all digits from a string.
Input: "My ID is 45 and pin is 9090"
Output: ['45', '9090']

'''
import re

text = "My ID is 45 and pin is 9090"
print(re.findall(r"\d+", text))
# ['45', '9090']

