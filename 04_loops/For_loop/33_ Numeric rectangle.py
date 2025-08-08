w = int(input("Enter width: "))
h = int(input("Enter height: "))
i = 1

while i <= h:
    j = 1
    while j <= w:
        print(i, end=" ")
        j += 1
    print()
    i += 1
