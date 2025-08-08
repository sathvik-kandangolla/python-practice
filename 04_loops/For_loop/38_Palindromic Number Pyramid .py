N = 5
i = 1
while i <= N:
    j = 1
    while j <= N - i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= i:
        print(k, end="")
        k += 1
    k = i - 1
    while k >= 1:
        print(k, end="")
        k -= 1
    print()
    i += 1
