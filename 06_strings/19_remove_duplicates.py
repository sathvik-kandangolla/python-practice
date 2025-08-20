'''Remove Consecutive Duplicates

Input: "aaabbcddd"
Expected Output: "abcd"
''' 

def remove_consecutive(s):
    result = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            result += s[i]
    return result

print(remove_consecutive("aaabbcddd"))
