'''
Count frequency of each letter in "apple".
Input: "apple"
Expected Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}

'''
s = "apple"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
