'''Longest palindromic substring

Input: "babad"
Output: "bab" (or "aba")'''

s = "babad"
res = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1] and len(sub) > len(res):
            res = sub
print(res)
