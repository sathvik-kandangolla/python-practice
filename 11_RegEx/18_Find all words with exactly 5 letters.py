'''
Find all words with exactly 5 letters

Input:

text = "Hello world regex works great"


Expected Output:

['Hello', 'world', 'regex', 'great']

'''
import re 

text = "Hello world regex works great"
print(re.findall(r"\b\w{5}\b", text))
# ['Hello', 'world', 'regex', 'great']
