x, y = map(bool, input().split())
if x and y:
    print("both true")
elif x and not y:
    print("first true only")
elif not x and y:
    print("second true only")
else:
    print("both false")