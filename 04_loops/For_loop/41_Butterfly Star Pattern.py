N = 4
i = 1
# Upper Half
while i <= N:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    space = 1
    while space <= 2 * (N - i):
        print(" ", end="")
        space += 1
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

# Lower Half
i = N
while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    space = 1
    while space <= 2 * (N - i):
        print(" ", end="")
        space += 1
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i -= 1
