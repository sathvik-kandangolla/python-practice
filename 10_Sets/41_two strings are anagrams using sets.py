'''
Write a Python program to check if two strings are anagrams using sets.
input :

s1 = "listen"
s2 = "silent"



Output:

True

'''

s1 = "listen"
s2 = "silent"
print(set(s1) == set(s2))
