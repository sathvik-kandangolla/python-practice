f1, f2 = map(bool, input().split())
if (f1 and not f2) or (not f1 and f2):
    print("One true")
elif f1 and f2:
    print("Both true")
else:
    print("Both false")