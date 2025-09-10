'''
Validate an Indian phone number (10 digits, starts with 6–9).
Input: "9876543210" → Output: True
Input: "1234567890" → Output: False

'''

import re 

phone1 = "9876543210"
phone2 = "1234567890"

pattern = r"^[6-9]\d{9}$"
print(bool(re.match(pattern, phone1)))  # True
print(bool(re.match(pattern, phone2)))  # False
