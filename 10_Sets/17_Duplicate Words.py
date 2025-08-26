'''
Find Duplicate Words Across Sentences

Input:
s1 = "apple banana orange grape"
s2 = "banana grape mango apple"

Expected Output:
{'banana', 'apple', 'grape'}
'''

s1 = "apple banana orange grape"
s2 = "banana grape mango apple"

set1 = set(s1.split())
set2 = set(s2.split())

print(set1 & set2)

