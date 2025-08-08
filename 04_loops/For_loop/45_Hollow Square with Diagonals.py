N = 5
i = 0
while i < N:
    j = 0
    while j < N:
        if i == 0 or i == N - 1 or j == 0 or j == N - 1 or i == j or j == N - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
