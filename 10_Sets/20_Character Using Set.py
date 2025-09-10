'''
First Non-Repeating Character Using Set
input :

s = "swiss"
Output:

w
'''
s = "swiss"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break

