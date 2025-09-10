'''
Extract all hashtags from a text.
Input: "I love #Python and #Coding"
Output: ['#Python', '#Coding']

'''

import re 

text = "I love #Python and #Coding"
print(re.findall(r"#\w+", text))
# ['#Python', '#Coding']
