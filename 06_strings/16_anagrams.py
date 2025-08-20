'''Check if two strings are anagrams

Input: "listen", "silent"
Expected Output: Yes'''

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))
