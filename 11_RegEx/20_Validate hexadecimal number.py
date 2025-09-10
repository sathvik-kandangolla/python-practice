'''
Validate if a string is a valid hexadecimal number (only 0-9, A-F).

Input:

"1A3F"


Expected Output:

True


Input:

"123G"


Expected Output:

False

'''
hex1 = "1A3F"
hex2 = "123G"

import re 

pattern = r"^[0-9A-F]+$"
print(bool(re.match(pattern, hex1)))  # True
print(bool(re.match(pattern, hex2)))  # False

