a, b, c = map(int, input().split())
if a + b + c != 180:
    print("Invalid triangle")
else:
    if a < 90 and b < 90 and c < 90:
        print("acute")
    elif a == 90 or b == 90 or c == 90:
        print("right")
    else:
        print("obtuse")