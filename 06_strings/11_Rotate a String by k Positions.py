s = "hello"
k = 2
k %= len(s)
print(s[-k:] + s[:-k])
