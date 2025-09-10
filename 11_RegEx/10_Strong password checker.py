'''
Strong password checker (must contain at least 1 uppercase, 1 lowercase, 1 digit, and 1 special character, min length = 8).
Input: "Pass@123" → Output: True
Input: "weakpass" → Output: False

'''

import re 

password1 = "Pass@123"
password2 = "weakpass"

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
print(bool(re.match(pattern, password1)))  # True
print(bool(re.match(pattern, password2)))  # False
