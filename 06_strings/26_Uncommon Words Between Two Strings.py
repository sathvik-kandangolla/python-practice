'''Find Uncommon Words Between Two Strings
input:red blue green
input:blue yellow green 
Expected Output: uncommon'''

s1 = "red blue green"
s2 = "blue yellow red"
words1 = set(s1.split())
words2 = set(s2.split())
uncommon = list(words1 ^ words2)  # symmetric difference
print( uncommon)
