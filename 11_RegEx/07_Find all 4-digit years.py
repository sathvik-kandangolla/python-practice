'''
Find all 4-digit years in a text.
Input: "World War happened in 1945, Independence in 1947"
Output: ['1945', '1947']

'''

import re 
text = "World War happened in 1945, Independence in 1947"
print(re.findall(r"\b\d{4}\b", text))
# ['1945', '1947']
