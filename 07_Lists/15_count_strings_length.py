'''Count strings with length ≥ 2 and same first/last character

Input: ['abc', 'xyz', 'aba', '1221']
Output: 2'''


words = ['abc', 'xyz', 'aba', '1221']
count = 0
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
print(count)   
