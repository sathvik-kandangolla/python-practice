n = int(input())
if n % 3 == 0 and n % 7 == 0:
    print("Multiple of both 3 and 7")
elif n % 3 == 0:
    print("Multiple of 3")
elif n % 7 == 0:
    print("Multiple of 7")
else:
    print("None")