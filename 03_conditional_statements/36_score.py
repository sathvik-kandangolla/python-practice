score, extra = map(int, input().split())
if score >= 60 or score + extra >= 60:
    print("Pass")
else:
    print("Fail")