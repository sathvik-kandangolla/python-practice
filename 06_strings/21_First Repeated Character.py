'''Find First Repeated Character

Input: "abcade"
Expected Output: "a"'''

def first_repeated(s):
    seen = set()
    for ch in s:
        if ch in seen:
            return ch
        seen.add(ch)
    return None

print(first_repeated("abcade"))
