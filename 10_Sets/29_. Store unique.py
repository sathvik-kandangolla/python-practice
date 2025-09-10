'''
Store unique IP addresses visited on a website
ips = ["192.168.1.1", "10.0.0.2", "192.168.1.1", "10.0.0.3"]
Expected Output:

{'192.168.1.1', '10.0.0.2', '10.0.0.3'}
'''
ips = ["192.168.1.1", "10.0.0.2", "192.168.1.1", "10.0.0.3"]
unique_ips = set(ips)
print(unique_ips)
