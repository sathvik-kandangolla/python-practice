n = int(input("Enter the height of the pyramid: "))
i = 1
while i <= n:
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1
    j = 1
    while j <= (2 * i - 1):
        if i == n or j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
