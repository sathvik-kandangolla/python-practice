'''
Common Letters Across Multiple Words
input :

words = ["python", "typhoon", "phony"]
Output:

{'h', 'o', 'n', 'y'}

'''

words = ["python", "typhoon", "phony"]

common = set(words[0])
for w in words[1:]:
    common &= set(w)

print(common)
