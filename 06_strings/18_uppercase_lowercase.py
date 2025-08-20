'''Count Uppercase and Lowercase Letters

Input: "PyThOn"
Expected Output: Upper: 3, Lower: 3'''

def count_case(s):
    upper, lower = 0, 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

print(count_case("PyThOn"))
