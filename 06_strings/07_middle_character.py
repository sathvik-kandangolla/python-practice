s = "python"
mid = len(s)//2
if len(s) % 2 == 0:
    print("Middle characters:", s[mid-1], "and", s[mid])
else:
    print("Middle character:", s[mid])
