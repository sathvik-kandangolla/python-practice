a, b = map(float, input().split())
if abs(a - b) < 0.001:
    print("Same")
else:
    print("Different")