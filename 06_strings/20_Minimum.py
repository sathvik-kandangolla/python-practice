'''Minimum Characters to Add at Front to Make Palindrome

Input: "abc"
Expected Output: 2'''

def min_chars_palindrome(s):
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            return i
    return len(s)

print(min_chars_palindrome("abc"))
