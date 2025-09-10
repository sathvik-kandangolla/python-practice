'''
Extract all valid IP addresses

Input:

text = "My server IPs are 192.168.1.1 and 10.0.0.255"


Expected Output:

['192.168.1.1', '10.0.0.255']

'''
import re 

text = "My server IPs are 192.168.1.1 and 10.0.0.255"
print(re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text))
# ['192.168.1.1', '10.0.0.255']
