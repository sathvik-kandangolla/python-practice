'''String compression (like "aaabbc" → "a3b2c1")
Input: "aaabbc"
Expected Output: "a3b2c1"'''

s = input("Enter string: ")  # aaabbc
res = ""
count = 1
for i in range(1,len(s)):
    if s[i]==s[i-1]: count+=1
    else:
        res+=s[i-1]+str(count)
        count=1
res+=s[-1]+str(count)
print("Compressed string:", res)

