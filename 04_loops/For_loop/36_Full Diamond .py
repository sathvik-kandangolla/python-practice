N = 5
i = 1
# Upper half
while i <= N:
    j = 1
    while j <= N - i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1
    print()
    i += 1

i = N - 1
# Lower half
while i >= 1:
    j = 1
    while j <= N - i:
        print(" ", end="")
        j += 1
    k = 1
    while k <= (2 * i - 1):
        print("*", end="")
        k += 1
    print()
    i -= 1
