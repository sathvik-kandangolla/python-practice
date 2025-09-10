'''
Validate if a string is a valid email address.
Input: "test@gmail.com" → Output: True
Input: "wrong@email" → Output: False

'''
import re 
email1 = "test@gmail.com"
email2 = "wrong@email"

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$"
print(bool(re.match(pattern, email1)))  # True
print(bool(re.match(pattern, email2)))  # False
