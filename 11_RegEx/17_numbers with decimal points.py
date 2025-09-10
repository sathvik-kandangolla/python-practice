'''
Extract all numbers with decimal points

Input:

text = "The values are 45.67, 100, and 23.5"


Expected Output:

['45.67', '23.5']

'''
import re 

text = "The values are 45.67, 100, and 23.5"
print(re.findall(r"\d+\.\d+", text))
# ['45.67', '23.5']
