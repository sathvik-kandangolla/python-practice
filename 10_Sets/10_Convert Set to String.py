'''
ython program to convert Set to String
Story: You turn your collection of letters into a cool code word.
Sample Input:
letters = {"A", "B", "C"}
Sample Output:
"BAC"

'''
letters = {"A", "B", "C"}
print("".join(sorted(letters)))
