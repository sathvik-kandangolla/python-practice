'''Check if a String is Palindrome
Input: "madam"
Expected Output: yes
'''
s = "madam"
if s == s[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")
