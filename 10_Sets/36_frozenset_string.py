'''
How do you convert a frozenset of characters to a string?
input :
fs = frozenset(['h', 'e', 'l', 'o'])


Output :

helo

'''

fs = frozenset(['h', 'e', 'l', 'o'])
s = "".join(fs)
print(s)
