N = int(input("Enter the height of the diamond : "))
if N % 2 == 0:
    print("5")
else:
    i = 1
    while i <= N // 2 + 1:
        j = 1
        while j <= N // 2 + 1 - i:
            print(" ", end="")
            j += 1
        j = 1
        while j <= 2 * i - 1:
            print("*", end="")
            j += 1
        print()
        i += 1

   
    i = N // 2
    while i >= 1:
        j = 1
        while j <= N // 2 + 1 - i:
            print(" ", end="")
            j += 1
        j = 1
        while j <= 2 * i - 1:
            print("*", end="")
            j += 1
        print()
        i -= 1