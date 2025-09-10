'''
Split a sentence by spaces using regex.
Input: "Regex is powerful"
Output: ['Regex', 'is', 'powerful']

'''

import re 

text = "Regex is powerful"
print(re.split(r"\s+", text))
# ['Regex', 'is', 'powerful']
