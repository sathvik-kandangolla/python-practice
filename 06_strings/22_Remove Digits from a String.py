'''Remove Digits from a String

Input: "he11o123"
Expected Output: "heo"'''

def remove_digits(s):
    result = ""
    for ch in s:
        if not ch.isdigit():
            result += ch
    return result

print(remove_digits("he11o123"))  
