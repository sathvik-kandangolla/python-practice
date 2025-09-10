'''
Extract time in HH:MM format

Input:

text = "The train departs at 09:45 and arrives at 18:30"


Expected Output:

['09:45', '18:30']

'''
import re 

text = "The train departs at 09:45 and arrives at 18:30"
print(re.findall(r"\b\d{2}:\d{2}\b", text))
# ['09:45', '18:30']
