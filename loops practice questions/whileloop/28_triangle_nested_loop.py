N = int(input("Enter the number of rows: "))
i = 1
while i <= N:
    j = 1
    while j <= i:
        print(i, end="")
        j += 1
    print()
    i += 1
    