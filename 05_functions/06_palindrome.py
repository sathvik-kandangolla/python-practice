def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1] 
print(is_palindrome("Racecar"))  # Output: True
print(is_palindrome("Hello"))    # Output: False 