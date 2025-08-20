s = "abcde"
temp = s + s
for i in range(1, len(s)+1):
    if temp[i:i+len(s)] == s:
        print(i)
        break
