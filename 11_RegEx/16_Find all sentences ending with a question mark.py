'''
Find all sentences ending with a question mark

Input:

text = "What is your name? My name is Sathvik. How are you?"


Expected Output:

['What is your name?', 'How are you?']

'''
import re 

text = "What is your name? My name is Sathvik. How are you?"
print(re.findall(r"[^.?!]*\?", text))
# ['What is your name?', 'How are you?']
