N = 5
i = 0
while i < N:
    j = 0
    while j < N:
        if i == j or j == N - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
