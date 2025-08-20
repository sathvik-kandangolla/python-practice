s = "madam"

# Palindrome check
is_palindrome = s == s[::-1]

# Symmetrical check
mid = len(s) // 2
is_symmetrical = s[:mid] == s[-mid:]

print("Palindrome:", "Yes" if is_palindrome else "No")
print("Symmetrical:", "Yes" if is_symmetrical else "No")
