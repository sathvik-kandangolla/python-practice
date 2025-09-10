'''
Find all words ending with "ing"

Input:

text = "I am learning coding and running daily"


Expected Output:

['learning', 'coding', 'running']

'''
import re

text = "I am learning coding and running daily"
print(re.findall(r"\b\w+ing\b", text))
# ['learning', 'coding', 'running']
