N = int(input("Enter the height of the pyramid: "))
i = 1
while i <= N:
    j = 1
    while j <= N - i:
        print(" ", end="")
        j += 1
    j = 1
    while j <= (2 * i - 1):
        if str(j) == str(j)[::-1]:  

            print(j, end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1