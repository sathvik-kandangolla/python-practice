'''Find First Non-Repeating Character

Input: "aabbccdeff"
Expected Output: "d"'''

s = "aabbccdeff"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

