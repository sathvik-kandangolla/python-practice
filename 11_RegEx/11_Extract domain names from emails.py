'''
Extract domain names from a list of emails.
Input: ["abc@gmail.com", "xyz@yahoo.in"]
Output: ['gmail.com', 'yahoo.in']

'''
import re 

emails = ["abc@gmail.com", "xyz@yahoo.in"]
domains = [re.search(r"@(.+)", email).group(1) for email in emails]
print(domains)
# ['gmail.com', 'yahoo.in']
