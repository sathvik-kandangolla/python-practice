'''Check if a String is Valid Shuffle of Two Strings

Input: "abc", "def", "dabecf"
Expected Output: Yes'''

def is_shuffle(s1, s2, s3):
    return sorted(s1+s2) == sorted(s3)

print(is_shuffle("abc", "def", "dabecf"))
